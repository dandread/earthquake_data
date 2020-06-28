#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:17:53 2020

@author: dominickdandrea
"""


import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data.
filename = '1.0_month.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)
   
#Store earthquake features in a variable.    
all_eq_dicts = all_eq_data['features']

#Extract the magnitude and coordinates of each earthquake and insert into list.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
    
#Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'RdYlGn',
        'reversescale': True,
        'colorbar': {"title": 'Magnitude'}
        },
}]

my_layout = Layout(title='Global Earthquakes Over Past 30 Days')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
    