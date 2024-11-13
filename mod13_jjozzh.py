import unittest
import re
from datetime import datetime

# Create functions to validate inputs
def is_valid_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def is_valid_chart_type(chart_type):
    return chart_type in ['1', '2']

def is_valid_time_series(time_series):
    return time_series in ['1', '2', '3', '4']

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Create class TestStockVisualizerInputs
class TestStockVisualizerInputs(unittest.TestCase):

    # Test for symbol validation uppercase (use AAPL)
    def test_valid_symbol(self):
        self.assertTrue(is_valid_symbol("AAPL"))  

    # Test for lowercase
    def test_invalid_symbol_lowercase(self):
        self.assertFalse(is_valid_symbol("aapl"))  

    # Test for invaild length (8 characters)
    def test_invalid_symbol_length(self):
        self.assertFalse(is_valid_symbol("ABCDEFGH"))  

    # Test for invaild symbol with numeric
    def test_invalid_symbol_numeric(self):
        self.assertFalse(is_valid_symbol("AAPL123")) 

    # Test for chart type validation (1 - 2)
    def test_valid_chart_type_1(self):
        self.assertTrue(is_valid_chart_type("1"))  

    def test_valid_chart_type_2(self):
        self.assertTrue(is_valid_chart_type("2"))  

    # Test for invail chart type (3)
    def test_invalid_chart_type(self):
        self.assertFalse(is_valid_chart_type("3"))  

    # Test for time series validation (1 or 4)
    def test_valid_time_series(self):
        self.assertTrue(is_valid_time_series("1")) 
        self.assertTrue(is_valid_time_series("4"))  

    # Test for invaild time series (6)
    def test_invalid_time_series(self):
        self.assertFalse(is_valid_time_series("6"))  

    # Test for start date validation ("2024-08-02")
    def test_valid_start_date(self):
        self.assertTrue(is_valid_date("2024-08-02"))

    # Test for start date with invalid format
    def test_invalid_start_date_format(self):
        self.assertFalse(is_valid_date("10/11/2024"))  
        self.assertFalse(is_valid_date("2024/11/10"))  

    #Test for start date with characters
    def test_invalid_start_date_characters(self):
        self.assertFalse(is_valid_date("2024-09-JK"))

    # Test for end date validation ("2024-12-31")
    def test_valid_end_date(self):
        self.assertTrue(is_valid_date("2024-09-02"))  

    # Test for end date with invaild format
    def test_invalid_end_date_format(self):
        self.assertFalse(is_valid_date("15-01-2001"))
        self.assertFalse(is_valid_date("10/11/2024"))  
    
    # Test for end date with characters
    def test_invalid_end_date_characters(self):
        self.assertFalse(is_valid_date("2001-12-AB"))    

if __name__ == "__main__":
    unittest.main()
