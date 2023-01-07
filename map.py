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
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+" m" ,fill_color=color_producer(el),color="pink",fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding = 'unicode_escape').read())))

    
map.add_child(fg)
map.save("map1.html")