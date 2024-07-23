import pytest
import random
from unittest.mock import patch
import sys
import io

# Assume the main function is in a file called exercise_3.py
from exercise_3 import main, num_digits


def test_main_function_exists():
    assert 'main' in globals(), "main function is not defined"


def run_with_input(input_value):
    input_mock = lambda _: input_value
    output = io.StringIO()

    with patch('builtins.input', input_mock):
        with patch('sys.stdout', output):
            main()

    return output.getvalue()


def test_main_multiple_digits():
    x = str(random.randint(10, 100000))
    expected_output = f"{x} has {len(str(x))} digits.\n"
    assert run_with_input(x) == expected_output


def test_main_single_digit():
    x = str(random.randint(1, 9))
    expected_output = f"{x} has {len(str(x))} digit.\n"
    assert run_with_input(x) == expected_output


def test_main_invalid_input():
    x = "test"
    expected_output = "Invalid input.\n"
    assert run_with_input(x) == expected_output


@pytest.mark.parametrize("number, expected", [
    (1, 1),
    (23, 2),
    (24626, 5),
    (2525, 4),
    (262627, 6),
    (10 ** 6, 7)
])
def test_num_digits(number, expected):
    assert num_digits(number) == expected