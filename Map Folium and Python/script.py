import folium

map=folium.Map(location=[9.0778, 8.6775],zoom_start=12, tiles='Stamen Terrain')

tooltip='Click me!'

folium.Marker(location=[5.532003041, 7.486002487],popup='Abia',icon=folium.Icon(color='red')).add_to(map)
folium.Marker(location=[10.2703408, 13.2700321],popup='Adamawa',icon=folium.Icon(color='green')).add_to(map)
folium.Marker(location=[5.007996056, 7.849998524],popup='Akwa Ibom',icon=folium.Icon(color='blue')).add_to(map)
folium.Marker(location=[9.05785, 7.49508],popup='Abuja State',icon=folium.Icon(color='orange')).add_to(map)
folium.Marker(location=[7.401962, 3.917313],popup='Ibadan state',icon=folium.Icon(color='darkred')).add_to(map)
folium.Marker(location=[5.544230, 5.760269],popup='Warri, Delta, state',icon=folium.Icon(color='lightgreen')).add_to(map)
folium.Marker(location=[6.465422, 3.406448],popup='Lagos state',icon=folium.Icon(color='purple')).add_to(map)

map.save('Nigerian.html')
