"""
This module is intended import data stored in csv's located in the
GradPads/data directory. The csv's are obtained from
https://www.zillow.com/research/data/. The zip code list
"""

import pandas as pd
import os

def GP_dataframe_import(filename):
    path = os.path.join('..', 'data', filename)
    df = pd.read_csv(path)
    return df

def zillow_df(df, region_list, region_column_str, columns_list):
    #Takes a dataframe as input
    df = df[df[region_column_str].isin(region_list)]
    df = df[columns_list]
    df[region_column_str] = df[region_column_str].astype(str)
    return df

def zillow_dict(df):
    dict = df.set_index('RegionName')['2018-09']
    return dict

def date_filter(df, date_column, year):
    df[date_column] = pd.to_datetime(df[date_column])
    df = df[df[date_column] > pd.Timestamp(year,1,1)]
    return df
