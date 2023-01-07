import folium
import pandas
map = folium.Map(location=[38.87,-99.1],zoom_start=6,tiles="Stamen Terrain")
data = pandas.read_csv("4.1 Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])

fg = folium.FeatureGroup(name="my map")


for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup="hi i am here",icon=folium.Icon(color='green')))



    
map.add_child(fg)
map.save("map1.html")