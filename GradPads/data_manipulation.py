"""
This module is intended import data stored in csv's located in the
GradPads/data directory. The csv's are obtained from
https://www.zillow.com/research/data/. The zip code list
"""

import pandas as pd

def zillow_df(df, region_list, region_column_str, columns_list):
    #Takes a dataframe as input
    df = df[df[region_column_str].isin(region_list)]
    df = df[columns_list]
    df[region_column_str] = df[region_column_str].astype(str)
    return df

def zillow_dict(df):
    dict = df.set_index('RegionName')['2018-09']
    return dict
