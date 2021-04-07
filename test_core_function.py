# DOCUMENTATION: this script contains the test function that will check the validity of price() function.

from core_function import price

def test_price():
    assert price(5, 0.3, 4, 0.7) == 4.3
    