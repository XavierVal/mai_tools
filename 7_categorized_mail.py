import re

# Training examples
training_examples = [
    "os paso nuevo pedido",
    "adjuntamos nuevo pedido",
    "envío pedido urgente",
    "pedido para la tienda de albacete",
    "pedido colchón 135x190cm viscoelástico",
    "nuevo pedido para entrega inmediata",
    "referencia: maria ramos mouhoub",
    "enviar al almacen de",
    "new order"
]

# Known auto sender patterns
known_auto_senders = [
    "soporte@buensueno.es",
    "noreply@", "no-reply@",
    "info@", "notificaciones@", "newsletter@", "sistemas@", "automatico@", "buensueno.es"
]

def is_auto_sender(from_):
    """Return True if the sender's email contains one of the known auto sender patterns."""
    return any(pattern in from_ for pattern in known_auto_senders)

def similarity_score(text, examples):
    """Calculate a score by comparing the text to training examples."""
    score = 0
    for ex in examples:
        if ex in text:
            score += 15
        # Check if the first word of the example is present in the text
        elif ex.split()[0] in text:
            score += 5
    return score

# Simulated email data structure for demonstration
class Email:
    def __init__(self, json_data):
        self.json = json_data

# Sample list of emails (populate with actual Email objects)
emails = []  # This should be a list of Email objects with a 'json' attribute

results = []

for email in emails:
    subject = email.json.get('subject', '')
    body = email.json.get('body', '')
    snippet = email.json.get('snippet', '')
    from_ = email.json.get('from', '').lower()
    text = (subject + " " + body + " " + snippet).lower()

    # --- FILTERING AUTO SENDERS ---
    if is_auto_sender(from_):
        results.append({
            'json': {
                **email.json,
                '_metadata': {
                    'category': 'otros',
                    'subcategory': 'respuesta',
                    'isPotentialOrder': False,
                    'score': 0,
                    'rejectionReason': 'Remitente automático conocido'
                }
            }
        })
        continue

    # --- DETECTION RULES ---
    match_frase_pedido = bool(re.search(r"os\s+paso.{0,30}(pedido|orden|compra)", text)) or \
                          bool(re.search(r"adjuntamos.{0,30}(pedido|orden)", text))
    match_nuevo_pedido = bool(re.search(r"nuevo\s+pedido", text))
    match_palabra_clave = bool(re.search(r"\b(pedido|orden|compra|solicitud)\b", text))
    match_cantidad = bool(re.search(r"\b\d+\s*(unidad(es)?|uds?|piezas?)\b", text))
    match_medidas = bool(re.search(r"\b\d{2,3}x\d{2,3}(cm|mm|m)?\b", text))
    match_producto = bool(re.search(r"colch[oó]n|viscoel[aá]stico|almac[eé]n|referencia", text))
    has_attachments = len(email.json.get('attachments', [])) > 0

    score = 0
    if match_frase_pedido:
        score += 30
    if match_nuevo_pedido:
        score += 20
    if match_palabra_clave:
        score += 20
    if match_cantidad:
        score += 15
    if match_medidas:
        score += 10
    if match_producto:
        score += 5
    if has_attachments:
        score += 10

    # Add similarity based on training examples
    score += similarity_score(text, training_examples)

    is_potential_order = score >= 30

    # --- ASSIGNING CATEGORY & SUBCATEGORY ---
    if is_potential_order:
        category = 'pedido'
        # Check for a "nuevo pedido" or a match on an attached phrase
        if match_nuevo_pedido or re.search(r"adjuntamos.*nuevo.*pedido", text):
            subcategory = 'nuevo_pedido'
        else:
            subcategory = 'pedido_otro'
        rejection_reason = None
    else:
        category = 'otros'
        if re.search(r"informaci[oó]n|detalle|consultar|aclaraci[oó]n", text):
            subcategory = 'solicitud_informacion'
        elif re.search(r"estado|tracking|seguimiento|env[ií]o|llegada", text):
            subcategory = 'tracking'
        elif re.search(r"unsubscribe|baja|publicidad|oferta", text):
            subcategory = 'spam'
        else:
            subcategory = 'otros'

        rejection_reason = 'Sospecha de pedido, pero faltan datos clave' if score >= 20 else 'No parece un pedido'

    results.append({
        'json': {
            **email.json,
            '_metadata': {
                'category': category,
                'subcategory': subcategory,
                'isPotentialOrder': is_potential_order,
                'score': score,
                'rejectionReason': rejection_reason
            }
        }
    })

# Now the 'results' list contains the processed emails with the extra metadata.
return results

