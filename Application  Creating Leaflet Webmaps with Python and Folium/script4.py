import folium

map = folium.Map(
    location=[46.1991, -122.1889],
    tiles='Stamen Terrain',
    zoom_start=13
)

map.add_child(folium.LatLngPopup())

map.save('latlon.html')
