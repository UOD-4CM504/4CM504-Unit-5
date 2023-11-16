from exercise_5_1 import *

def test_calc_retail_price():
  assert calc_retail_price(5,40) == 7.0
  assert round(calc_retail_price(25.3,75),3) == 44.275
