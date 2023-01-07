import folium
import pandas
map = folium.Map(location=[38.87,-99.1],zoom_start=6,tiles="Stamen Terrain")
data = pandas.read_csv("4.1 Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

fg = folium.FeatureGroup(name="my map")

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return "yellow"
    else:
       return 'red'

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m" ,icon=folium.Icon(color=color_producer(el))))



    
map.add_child(fg)
map.save("map1.html")