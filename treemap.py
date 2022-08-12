import folium
from folium import Marker
import webbrowser
import os
import pandas as pd

# set chrome as browser
browser = webbrowser.get('chrome')

# import tree dataset and create new columns for longitude and latitude
trees = pd.read_csv('data/arbresremarquablesparis.csv', sep=';')
trees['latitude'] = trees['Geo point'].str.split(',').str.get(-1)
trees['longitude'] = trees['Geo point'].str.split(',').str.get(0)
print(trees.columns)
print(trees.head())

# create map
coords = [48.8566, 2.3522] # coordinates of Paris
map = folium.Map(location=coords, zoom_start=13)

# add markers for trees
for idx, row in trees.iterrows():
    Marker(location=[row['longitude'], row['latitude']],
    icon=folium.Icon(color='darkgreen', icon='tree-deciduous'),
    popup= row['LIBELLEFRANCAIS']
    ).add_to(map)

# save and display map
map.save('output/RemarkableTreesMap.html')
browser.open_new_tab('file://' + os.path.realpath('output/RemarkableTreesMap.html'))

