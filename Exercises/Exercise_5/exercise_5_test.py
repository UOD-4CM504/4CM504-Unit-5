import pytest
from unittest.mock import patch
import io
import sys
import inspect
import random

# Import the functions you want to test
from exercise_5 import get_user_guess, print_feedback, main


def test_get_user_guess():
    x = random.randint(1, 10)

    with patch('builtins.input', return_value=str(x)):
        result = get_user_guess()
        assert result == str(x)

    with patch('builtins.input', return_value="q"):
        result = get_user_guess()
        assert result == "q"


def test_main_function_exists():
    assert 'main' in globals(), "main function is not defined"


def test_get_user_guess_with_invalid_inputs():
    input_strs = [str(11), str(13), "S", str(10)]
    expected_output = ["Please enter a whole number between 1 and 10 or q to quit\n", "Invalid input\n\n",
                       "Please enter a whole number between 1 and 10 or q to quit\n", "Invalid input\n\n",
                       "Please enter a whole number between 1 and 10 or q to quit\n", "Invalid input\n\n",
                       "Please enter a whole number between 1 and 10 or q to quit\n"]

    output = []

    def mock_input_func(*args):
        if len(args) > 0:
            output.append(args[0])
        return input_strs.pop(0)

    def mock_print_func(*args, end="\n"):
        temp_str = ""
        if len(args) > 0:
            temp_str = " ".join([str(x) for x in args])
        output.append(f"{temp_str}{end}")

    with patch('builtins.input', side_effect=mock_input_func):
        with patch('builtins.print', side_effect=mock_print_func):
            try:
                get_user_guess()
            except Exception as e:
                output.append(f"Main method failed. {e}")

    assert "".join(output) == "".join(expected_output)


def test_print_feedback():
    assert 'print_feedback' in globals(), "print_feedback function is not defined"

    argspec = inspect.getfullargspec(print_feedback)
    arguments = argspec.args[:len(argspec.args) - len(argspec.defaults)] if argspec.defaults else argspec.args

    assert len(arguments) == 3, "Function print_feedback does not take in 3 positional arguments"

    # Test case 1
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_feedback(2, 3, 5)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Well done, you used 2/3 guesses to guess the secret number 5.\n"

    # Test case 2
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_feedback(3, 3, 6)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Well done, you used 3/3 guesses to guess the secret number 6.\n"

    # Test case 3
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_feedback(4, 3, 9)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Sorry, better luck next time.\n"


if __name__ == "__main__":
    pytest.main([__file__])