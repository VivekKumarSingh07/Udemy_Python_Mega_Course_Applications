import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
def color_producer(elevation):
	if elevation>1000:
		return 'green'
	elif elevation>3000:
		return 'orange'
	else:
		return 'red'

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58,-99.09],zoom_start = 6,tiles = "Mapbox Bright")

fgVolcanos = folium.FeatureGroup(name="Volcanos")
for la,lo,el in zip(lat,lon,elev):
	fgVolcanos.add_child(folium.CircleMarker(location = [la,lo],radius = 6, popup = str(el) + " m",
	fill = True,fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))


fgPopulation = folium.FeatureGroup(name="Population")
fgPopulation.add_child(folium.GeoJson(data=open("world.json",'r',encoding = 'utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<= x['properties']['POP2005']<=20000000 else 'red'}))


map.add_child(fgVolcanos)
map.add_child(fgPopulation)
map.add_child(folium.LayerControl())
map.save("Map.html")
