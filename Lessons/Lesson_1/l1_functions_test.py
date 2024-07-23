from l1_functions import *

def test_odd():
  assert odd_test(3) == True
  assert odd_test(9) == True
  assert odd_test(47) == True

def test_even():
  assert odd_test(2) == False
  assert odd_test(20) == False
  assert odd_test(32) == False
