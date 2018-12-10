"""This module generates the GradPads map of Seattle."""

import os
import folium
from branca.colormap import linear
import data_manipulation as dm

#Making lists to slice dataframes.
SEATTLE_ZIPS = [98125, 98133, 98177, 98117, 98107, 98103, 98115, 98105,
                98112, 98102, 98109, 98119, 98199, 98121, 98101, 98104,
                98122, 98144, 98134, 98108, 98118, 98106, 98126, 98116,
                98136]
ZILLOW_COLUMNS = ['RegionName', 'City', 'State', '2018-09']

#Specifying the filepaths for data import.
#studio_rental_path = os.path.join('..', 'data', 'Zip_MedianRentalPrice_Studio.csv')
#onebr_rental_path = os.path.join('..', 'data', 'Zip_MedianRentalPrice_1Bedroom.csv')

#Converting these csv's into dataframes.
try:
    studio_rental = dm.GP_dataframe_import('Zip_MedianRentalPrice_Studio.csv')
except FileNotFoundError as error:
    print(error)
    print('Is this file still in the data folder?')

try:
    onebr_rental = dm.GP_dataframe_import('Zip_MedianRentalPrice_1Bedroom.csv')
except FileNotFoundError as error:
    print(error)
    print('Is this file still in the data folder?')

#Slicing dataframes
studio_rental = dm.zillow_df(studio_rental, SEATTLE_ZIPS, 'RegionName', ZILLOW_COLUMNS)
onebr_rental = dm.zillow_df(onebr_rental, SEATTLE_ZIPS, 'RegionName', ZILLOW_COLUMNS)

#Making dictionaries to for mapping colormap values to zip code dataself.
studio_rental_dict = dm.zillow_dict(studio_rental)
onebr_rental_dict = dm.zillow_dict(onebr_rental)

"""
Making map layers
    ------------
"""
#Initializing a map centered on the UW.
m = folium.Map(location=[47.6553, -122.3035], zoom_start=12, min_zoom=10)

#Specifiying the path for zip code json data for generating map layersself.
zip_codes = os.path.join('..', 'data', 'wa_washington_zip_codes_geo.min.json')

#Adding a linear colormap for studio and one bedroom rental prices.
colormap = linear.YlOrRd_09.scale(1050, 2650)
colormap.caption = 'Monthly Rental Price in Dollars'
m.add_child(colormap)

#Studio Rental Price Layer
def style_function(feature):
    """A style function for mapping Zillow studio rental data when it's present."""
    if feature['properties']['ZCTA5CE10'] in studio_rental_dict:
        return {
            'fillOpacity' : 0.5,
            'weight' : 1,
            'fillColor': colormap(studio_rental_dict[feature['properties']['ZCTA5CE10']]),
            'color' : 'Black',
        }
    return {
        'fillColor': 'none',
        'weight' : 0.5,
        'line_opacity' : 0.5,
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
    """A style function for mapping Zillow one bedroom data when it's present."""
    if feature['properties']['ZCTA5CE10'] in onebr_rental_dict:
        return {
            'fillOpacity' : 0.5,
            'weight' : 1,
            'fillColor': colormap(onebr_rental_dict[feature['properties']['ZCTA5CE10']]),
            'color' : 'Black',
        }
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
transit = os.path.join(
    '..', 'data',
    'Transit_Routes_for_King_County_Metro__transitroute_line.geojson'
    )

def style_function3(feature):
    """A style function for mapping Transit route lines."""
    return {
        'fillColor': '#ffaf00',
        'line_opacity' : 0.5,
        'color': 'gray',
        'weight': 1.5,
        'dashArray': '5, 5'
    }

def highlight_function(feature):
    """A highlight function for Transit line mouseovers."""
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
    tooltip=folium.features.GeoJsonTooltip(
        ['ROUTE_NUM'], aliases=['Route Number'], interactive=True
    )
)

transit_geojson.add_to(m)


#                            Crime data
#                            ----------
#Crimes are categorized geographically by 'beats'. These are at about the
#neighborhood level. For instance, Ballard North and Ballard South.
#Directory file path for beat geojson data.
beats = os.path.join('..', 'data', 'SPD_Beats_WGS84.json')

#Importing the crime-data csv from the data folder
crime_df = dm.GP_dataframe_import('Crime_Data.csv')

#Editing the dataframe so that it only encompasses the past two years.
crime_df = dm.date_filter(crime_df, 'Occurred Date', 2017)
#Adding a count column for easy groupby summation
crime_df['Count'] = 1

#Making a layer for total crime incidents
total_crime_df = crime_df[['Occurred Date', 'Beat', 'Count']]

total_crime_per_beat = total_crime_df.groupby('Beat', as_index=False).sum()

total_crime_layer = folium.Choropleth(
    geo_data=beats,
    data=total_crime_per_beat,
    columns=['Beat', 'Count'],
    key_on='feature.properties.beat',
    fill_color='BuPu',
    nan_fill_color='none',
    line_weight=0.5,
    name='Total Crime Incidents',
    legend_name='Total Crime Incidents 2018'
)

total_crime_layer.add_to(m)
#Making a new dataframe that is grouped by both beat and crime category
theft_category_groupby = crime_df.groupby(['Beat', 'Crime Subcategory'], as_index=False).sum()
theft_category_groupby = theft_category_groupby[['Beat', 'Crime Subcategory', 'Count']]

#Making a bike-theft specific layer
bike_theft_groupby = theft_category_groupby[
    theft_category_groupby['Crime Subcategory'] == 'THEFT-BICYCLE']

bike_theft_layer = folium.Choropleth(
    geo_data=beats,
    data=bike_theft_groupby,
    columns=['Beat', 'Count'],
    key_on='feature.properties.beat',
    fill_color='BuPu',
    nan_fill_color='none',
    line_weight=0.5,
    name='Bike Theft',
    legend_name='Incidents of Bike Theft, Since 2017'
)

bike_theft_layer.add_to(m)

#Making a car prowl layer
car_prowl = theft_category_groupby[theft_category_groupby['Crime Subcategory'] == 'CAR PROWL']

car_prowl_layer = folium.Choropleth(
    geo_data=beats,
    data=car_prowl,
    columns=['Beat', 'Count'],
    key_on='feature.properties.beat',
    fill_color='BuPu',
    nan_fill_color='none',
    line_weight=0.5,
    name='Car Prowl',
    legend_name='Incidents of Car Prowl, Since 2017'
)

car_prowl_layer.add_to(m)

#Add layer control to our map and save it as an html
folium.LayerControl().add_to(m)
m.save('GradPads.html')
