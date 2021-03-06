import folium

map = folium.Map(
    location=[46.8527, -121.7649],
    tiles='Stamen Terrain',
    zoom_start=13
)

folium.Marker(
    [46.8354, -121.7325],
    popup='Camp Muir'
).add_to(map)

map.add_child(folium.ClickForMarker(popup='Waypoint'))


map.save('marker functionality.html')
