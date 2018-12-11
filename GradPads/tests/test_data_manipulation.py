"""A unit test for data_manipulation."""

import unittest
import pandas as pd
from GradPads import data_manipulation as dm


class TestZillowDfTestCase(unittest.TestCase):
    """Tests for test_zillow_df"""

    def test_columns_of_dataframe(self):
        """Test if zillow_df outputs the correct columns."""
        data_frame = pd.DataFrame({'yellow' : list(range(10)),
                                   'orange' : list(range(10)),
                                   'red' : list(range(10))
                                  })
        final_columns = ['yellow', 'orange']
        final_rows = [1, 2, 3, 4, 5]
        new_data_frame = dm.zillow_df(data_frame, final_rows, 'yellow', final_columns)
        self.assertTrue(new_data_frame.shape == (5, 2))

    def test_str_value_of_dataframe(self):
        """Test if zillow_df converts correct column to a string."""
        data_frame = pd.DataFrame({'yellow' : list(range(10)),
                                   'orange' : list(range(10)),
                                   'red' : list(range(10))
                                  })
        final_columns = ['yellow', 'orange']
        final_rows = [1, 2, 3, 4, 5]
        new_data_frame = dm.zillow_df(data_frame, final_rows, 'yellow', final_columns)
        self.assertTrue(isinstance(new_data_frame['yellow'][1], str))

class TestZillowDictTestCase(unittest.TestCase):
    """Tests for test_zillow_dict"""

    def test_zillow_dict_outputtype(self):
        """Tests if zillow_dict output is in correct form for mapping."""
        data_frame = pd.DataFrame({'RegionName' : list(range(10)),
                                   'Dummy Column' : list(range(10)),
                                   '2018-09' : list(range(10))
                                   })
        dseries = dm.zillow_dict(data_frame)
        self.assertTrue(isinstance(dseries, pd.Series))

    def test_zillow_dict_key(self):
        """Tests if the index is named correctly."""
        data_frame = pd.DataFrame({'RegionName' : list(range(10)),
                                   'Dummy Column' : list(range(10)),
                                   '2018-09' : list(range(10))
                                   })
        dseries = dm.zillow_dict(data_frame)
        self.assertTrue(dseries.index.name == 'RegionName')

class TestDateFilterTestCase(unittest.TestCase):
    """Tests for dm.date_filter"""

    def test_date_filter_year(self):
        """Tests if the remaining dates are more recent than the filter date."""
        data_frame = pd.DataFrame({
            'Dates' : ['01/10/2018', '01/11/2018', '01/12/2018', '12/10/2016'],
            'Dummy' : [1, 2, 3, 4]
            })
        data_frame = dm.date_filter(data_frame, 'Dates', 2017)
        self.assertTrue(data_frame['Dates'].min() > pd.Timestamp(2017, 1, 1))

    def test_date_filter_type(self):
        """Tests if the output has datetime type."""
        data_frame = pd.DataFrame({
            'Dates' : ['01/10/2018', '01/11/2018', '01/12/2018', '12/10/2016'],
            'Dummy' : [1, 2, 3, 4]
            })
        data_frame = dm.date_filter(data_frame, 'Dates', 2017)
        self.assertTrue(isinstance(data_frame['Dates'][1], pd.Timestamp))

if __name__ == '__main__':
    unittest.main()
