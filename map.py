import folium
import pandas

data = pandas.read_csv("4.1 Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return "yellow"
    else:
       return 'red'

map = folium.Map(location=[38.87,-99.1],zoom_start=6,tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+" m" ,
    fill_color=color_producer(el),color="gre",fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='unicode_escape').read(),
style_function=lambda x:{'fillcolor':'blue' if x['properties']['POP2005']<10000000 
else 'black' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

    
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")