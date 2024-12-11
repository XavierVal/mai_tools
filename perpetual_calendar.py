import calendar

def imprimir_calendario(mes, año):
    # Obtener el calendario del mes y año especificados
    calendario = calendar.monthcalendar(año, mes)

    # Determinar el nombre del mes
    nombre_mes = calendar.month_name[mes]

    # Imprimir el nombre del mes y el encabezado de los días de la semana
    print(f"Calendario de {nombre_mes} {año}:")
    print("L  M  M  J  V  S  D")

    # Iterar sobre las filas del calendario
    for semana in calendario:
        fila = ""
        for dia in semana:
            # Si el día es cero, significa que pertenece al mes anterior o siguiente
            if dia == 0:
                fila += "   "
            else:
                fila += f"{dia:2d} "
        print(fila)


# Solicitar al usuario el mes y año
try:
    mes = int(input("Introduce el número de mes (1-12): "))
    año = int(input("Introduce el año (ej. 2025): "))

    if 1 <= mes <= 12:
        imprimir_calendario(mes, año)
    else:
        print("Mes no válido. Debe estar en el rango de 1 a 12.")
except ValueError:
    print("Entrada no válida. Por favor, introduce un número de mes y año válidos.")