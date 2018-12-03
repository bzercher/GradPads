"""
This module is intended import data stored in csv's located in the
GradPads/data directory. The csv's are obtained from
https://www.zillow.com/research/data/. The zip code list
"""

import pandas as pd
import folium
import os

#Make a list of Seattle zip codes we are interested in.
seattle_zips = [98125, 98133, 98177, 98117, 98107, 98103, 98115, 98105,
                98112, 98102, 98109, 98119, 98199, 98121, 98101, 98104,
                98122, 98144, 98134, 98108, 98118, 98106, 98126, 98116,
                98136]

#Make a list of Zillow columns that we are interested in.
zillow_columns = ['RegionName', 'City', 'State', '2018-09']




def df_slicer(df, region_list, region_column_str, columns_list):
    #Takes a dataframe as input
    df = df[df[region_column_str].isin(region_list)]
    df = df[columns_list]
    df[region_column_str] = df[region_column_str].astype(str)
    print(df)
    return df
