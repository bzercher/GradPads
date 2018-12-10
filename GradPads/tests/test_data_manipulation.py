"""A unit test for data_manipulation."""

import unittest
import pandas as pd
import GradPads
from GradPads import data_manipulation as dm

"""python -m unittest GradPads.tests.test_data_manipulation"""

class test_zillow_dfTestCase(unittest.TestCase):
    """Tests for test_zillow_df"""

    def test_columns_of_dataframe(self):
        df = pd.DataFrame({'yellow' : list(range(10)),
                          'orange' : list(range(10)),
                          'red' : list(range(10))
                          })
        final_columns = ['yellow', 'orange']
        final_rows = [1, 2, 3, 4, 5]
        new_df = dm.zillow_df(df, final_rows, 'yellow', final_columns)
        self.assertTrue(new_df.shape == (5, 2))

    def test_str_value_of_dataframe(self):
        df = pd.DataFrame({'yellow' : list(range(10)),
                          'orange' : list(range(10)),
                          'red' : list(range(10))
                          })
        final_columns = ['yellow', 'orange']
        final_rows = [1, 2, 3, 4, 5]
        new_df = dm.zillow_df(df, final_rows, 'yellow', final_columns)
        self.assertTrue(type(new_df['yellow'][1]) == type('String'))

class test_zillow_dictTestCase(unittest.TestCase):
    """Tests for test_zillow_dict"""

    def test_zillow_dict_outputtype(self):
        df = pd.DataFrame({'RegionName' : list(range(10)),
                          'Dummy Column' : list(range(10)),
                          '2018-09' : list(range(10))
                          })
        dict = dm.zillow_dict(df)
        self.assertTrue(str(type(dict)) == "<class 'pandas.core.series.Series'>")

    def test_zillow_dict_Key(self):
        df = pd.DataFrame({'RegionName' : list(range(10)),
                          'Dummy Column' : list(range(10)),
                          '2018-09' : list(range(10))
                          })
        dict = dm.zillow_dict(df)
        self.assertTrue(dict.index.name == 'RegionName')

class test_date_filter_TestCase(unittest.TestCase):
    """Tests for dm.date_filter"""

    def test_date_filter_year(self):
        data_frame = pd.DataFrame({'Dates' : ['01/10/2018', '01/11/2018', '01/12/2018', '12/10/2016'],
                           'Dummy' : [1, 2, 3, 4]
                           })
        data_frame = dm.date_filter(data_frame, 'Dates', 2017)
        self.assertTrue(data_frame['Dates'].min() > pd.Timestamp(2017,1,1))

    def test_date_filter_type(self):
        data_frame = pd.DataFrame({'Dates' : ['01/10/2018', '01/11/2018', '01/12/2018', '12/10/2016'],
                           'Dummy' : [1, 2, 3, 4]
                           })
        data_frame = dm.date_filter(data_frame, 'Dates', 2017)
        self.assertTrue(str(type(data_frame['Dates'])=="<class 'pandas._libs.tslibs.timestamps.Timestamp'>"))

if __name__ == '__main__':
    unittest.main()
