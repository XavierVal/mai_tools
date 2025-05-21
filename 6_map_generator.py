import folium

# Crear un mapa centrado en Aigüestortes
map_demo = folium.Map(location=[42.6000, 0.3000], zoom_start=10)

# Lugares a visitar
lugares_a_visitar = [
    {'nombre': 'Estany de Sant Maurici', 'ubicación': [42.6000, 0.3000]},
    {'nombre': 'Riu Escrita', 'ubicación': [42.6050, 0.3050]},
    {'nombre': 'Montardo', 'ubicación': [42.6500, 0.2500]},
    {'nombre': 'Ratera', 'ubicación': [42.6400, 0.2900]},
    {'nombre': 'Peguera', 'ubicación': [42.6200, 0.2800]},
    {'nombre': 'Monestero', 'ubicación': [42.6100, 0.3100]}
]

# Agregar marcadores para lugares a visitar
for lugar in lugares_a_visitar:
    folium.Marker(location=lugar['ubicación'], popup=lugar['nombre']).add_to(map_demo)

# Campings
campings = [
    {'nombre': 'Camping Els Roures', 'ubicación': [42.6000, 0.3000]},
    {'nombre': 'Camping La Mola', 'ubicación': [42.6050, 0.3050]},
    {'nombre': 'Camping Boneta', 'ubicación': [42.6100, 0.2900]},
    {'nombre': 'Voraparc Camping', 'ubicación': [42.6200, 0.2800]},
    {'nombre': 'Nou Camping', 'ubicación': [42.6150, 0.2950]}
]

# Agregar marcadores para campings con icono verde
for camping in campings:
    folium.Marker(location=camping['ubicación'], popup=camping['nombre'], icon=folium.Icon(color='green')).add_to(map_demo)


# Rutas de cada día
rutas = [
    {'día': 'Viernes', 'ruta': [[39.4697, -0.3763], [42.6000, 0.3000]]},  # Valencia a Espot
    {'día': 'Sábado', 'ruta': [[42.6000, 0.3000], [42.6050, 0.3050], [42.6500, 0.2500]]},  # Espot a Montardo
    {'día': 'Domingo', 'ruta': [[42.6500, 0.2500], [42.6400, 0.2900], [42.6200, 0.2800]]},  # Montardo a Peguera
    {'día': 'Lunes', 'ruta': [[42.6200, 0.2800], [42.6100, 0.3100], [42.6000, 0.3000]]},  # Peguera a Espot
    {'día': 'Martes', 'ruta': [[42.6000, 0.3000], [42.6150, 0.2950], [42.6400, 0.2900]]},  # Espot a Ratera
    {'día': 'Miércoles', 'ruta': [[42.6400, 0.2900], [39.4697, -0.3763]]}  # Ratera a Valencia
]

# Agregar rutas al mapa
for ruta in rutas:
    folium.PolyLine(ruta['ruta'], color='blue', popup=f"Ruta del {ruta['día']}").add_to(map_demo)


# Guardar el mapa en un archivo HTML
map_demo.save('map.html')


