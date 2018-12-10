"""
This module is intended import data stored in csv's located in the
GradPads/data directory. The csv's are obtained from
https://www.zillow.com/research/data/. The zip code list
"""

import os
import pandas as pd

def gp_dataframe_import(filename):
    """
    Imports csvs from data folder into pandas dataframes.
    Takes the filename (with .csv extension) as a string as input.
    """
    path = os.path.join('..', 'data', filename)
    frame = pd.read_csv(path)
    return frame

def zillow_df(frame, region_list, region_column_str, columns_list):
    """
    Manipulates data obtained from Zillow.
    Input:
        dataframe;
        list, type corresponds to the region identifier in the dataframe;
        string, identifies the region column of the dataframe
        list, of columns that want to be kept
    """
    frame = frame[frame[region_column_str].isin(region_list)]
    frame = frame[columns_list]
    frame[region_column_str] = frame[region_column_str].astype(str)
    return frame

def zillow_dict(frame):
    """Takes a dataframe as input, outputs series that mimics a dictionary for
    colorscale mapping"""
    colormap_series = frame.set_index('RegionName')['2018-09']
    return colormap_series

def date_filter(frame, date_column, year):
    """Filters crime data by date
    Input:
        dataframe;
        string, identifies column that contains dates;
        int, filters any data from that year or older
    """
    frame[date_column] = pd.to_datetime(frame[date_column])
    frame = frame[frame[date_column] > pd.Timestamp(year, 1, 1)]
    return frame
