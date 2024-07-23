import pytest
from exercise_4 import arithmetic_sum

@pytest.mark.parametrize("a, d, n, expected", [
    (1, 1, 100, 5050),
    (2, 5, 45, 5040),
    (10, 4, 5, 90),
    (1, 2, 1000, 1000000),
    (-5, -2, 20, -480),
    (3, 2, 15, 255)
])
def test_arithmetic_sum(a, d, n, expected):
    assert arithmetic_sum(a, d, n) == expected