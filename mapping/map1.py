import folium
import pandas

data = pandas.read_csv("C://Users//busnu//Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
el = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.89], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, el):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" mts", parse_html=True, icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map1.html")
