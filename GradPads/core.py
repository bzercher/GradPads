import pandas as pd
import folium
import os
import data_manipulation as dm
from branca.colormap import linear

#Making lists to slice dataframes.
seattle_zips = [98125, 98133, 98177, 98117, 98107, 98103, 98115, 98105,
                98112, 98102, 98109, 98119, 98199, 98121, 98101, 98104,
                98122, 98144, 98134, 98108, 98118, 98106, 98126, 98116,
                98136]
zillow_columns = ['RegionName', 'City', 'State', '2018-09']

#Specifying the filepaths for data import.
studio_rental_path = os.path.join('..', 'data', 'Zip_MedianRentalPrice_Studio.csv')
onebr_rental_path = os.path.join('..', 'data', 'Zip_MedianRentalPrice_1Bedroom.csv')

#Converting these csv's into dataframes.
try:
    studio_rental = pd.read_csv(studio_rental_path)
except FileNotFoundError as error:
    print(error)
    print('Is the relative path still correct?')

try:
    onebr_rental = pd.read_csv(onebr_rental_path)
except FileNotFoundError as error:
    print(error)
    print('Is the relative path still correct?')

#Slicing dataframes
studio_rental = dm.zillow_df(studio_rental, seattle_zips, 'RegionName', zillow_columns)
onebr_rental = dm.zillow_df(onebr_rental, seattle_zips, 'RegionName', zillow_columns)

#Making dictionaries to for mapping colormap values to zip code dataself.
studio_rental_dict = dm.zillow_dict(studio_rental)
onebr_rental_dict = dm.zillow_dict(onebr_rental)

"""
Making our map layers
    ------------
"""
#Initializing a map centered on the UWself.
m = folium.Map(location=[47.6553, -122.3035], zoom_start=12, min_zoom=10)

#Specifiying the path for zip code json data for generating map layersself.
zip_codes = os.path.join('..', 'data', 'wa_washington_zip_codes_geo.min.json')

#Adding a linear colormap for studio and one bedroom rental prices.
colormap = linear.YlOrRd_09.scale(1050, 2650)
m.add_child(colormap)

#Studio Rental Price Layer
def style_function(feature):
    if feature['properties']['ZCTA5CE10'] in studio_rental_dict:
        return {
        'fillOpacity' : 0.5,
        'weight' : 1,
        'fillColor': colormap(studio_rental_dict[feature['properties']['ZCTA5CE10']]),
        'color' : 'Black',
        }
    else:
        return {
            'fillColor': 'none',
            'weight' : 0,
            'line_opacity' : 0.1,
            'color': 'Black',
        }

studio_geojson = folium.GeoJson(
    zip_codes,
    name='Average Monthly Rent for a Studio Apartment',
    style_function=style_function,
)

studio_geojson.add_to(m)

#Adding one bedroom rental price layer.
def style_function_2(feature):
    if feature['properties']['ZCTA5CE10'] in onebr_rental_dict:
        return {
        'fillOpacity' : 0.5,
        'weight' : 1,
        'fillColor': colormap(onebr_rental_dict[feature['properties']['ZCTA5CE10']]),
        'color' : 'Black',
        }
    else:
        return {
            'fillColor': 'none',
            'weight' : 0,
            'line_opacity' : 0.1,
            'color': 'Black',
        }

onebr_geojson = folium.GeoJson(
    zip_codes,
    name='Average Monthly Rent for a One Bedroom Apartment',
    style_function=style_function_2,
)

onebr_geojson.add_to(m)

#Add greenspace data
greenspace = os.path.join('..', 'data', 'greenspace2.geojson')

greenspace_geojson = folium.GeoJson(
    greenspace,
    name="Greenspace Markers",
    show=False
)

greenspace_geojson.add_to(m)

#Add Transit Route Data
transit = os.path.join('..', 'data', 'Transit_Routes_for_King_County_Metro__transitroute_line.geojson')

def style_function3(feature):
    return {
        'fillColor': '#ffaf00',
        'line_opacity' : 0.5,
        'color': 'gray',
        'weight': 1.5,
        'dashArray': '5, 5'
    }

def highlight_function(feature):
    return{
        'fillColor': '#ffaf00',
        'line_opacity' : 1,
        'color': 'blue',
        'weight': 3,
    }


transit_geojson = folium.GeoJson(
    transit,
    name="Transit Routes",
    show=False,
    style_function=style_function3,
    highlight_function=highlight_function,
    tooltip=folium.features.GeoJsonTooltip(['ROUTE_NUM'], aliases=['Route Number'], interactive=True)
)

transit_geojson.add_to(m)

#Add layer control to our map and save it as an html
folium.LayerControl().add_to(m)
m.save('GradPads.html')
