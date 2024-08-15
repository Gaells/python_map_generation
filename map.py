import folium
import pdfkit

# Coordenadas da UFPR Campus Politécnico
latitude = -25.4484
longitude = -49.2329

# Crie o mapa baseado na localização
map_center = [latitude, longitude]
mymap = folium.Map(location=map_center, zoom_start=16)  # Zoom ajustado para uma visão mais próxima do campus

folium.Marker(
    [latitude, longitude],
    popup="UFPR Campus Politécnico",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mymap)

# Salve o mapa como HTML
mymap.save("mymap.html")
print("Mapa salvo como mymap.html")

