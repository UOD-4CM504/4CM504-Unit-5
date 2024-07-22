# test_exercise_1.py

from exercise_1 import *
import pytest
from unittest.mock import patch
from io import StringIO

def test_calc_retail_price():
    assert calc_retail_price(5, 40) == 7.0
    assert round(calc_retail_price(25.3, 75), 3) == 44.275

@pytest.mark.timeout(2)
def test_main():
    function_name_to_check = 'main'
    assert function_name_to_check in globals(), "main function not defined"

    def run_test(test_values, expected_output):
        input_values = test_values
        output = StringIO()

        def mock_input(prompt):
            print(prompt, end='')
            return input_values.pop(0)

        with patch('builtins.input', mock_input), patch('sys.stdout', output):
            try:
                main()
            except Exception as e:
                pytest.fail(f"Main method failed. {e}")

        actual_output = output.getvalue()
        assert actual_output == expected_output, f"Expected:\n{expected_output}\nGot:\n{actual_output}"

    run_test(['10', '36'],
        'Please enter a wholesale cost:\n'
        'Please enter a markup percentage:\n'
        f"The retail price is £{13.60:.2f}.\n"
    )

    run_test(['100', '52.3'],
        'Please enter a wholesale cost:\n'
        'Please enter a markup percentage:\n'
        f"The retail price is £{152.30:.2f}.\n"
    )

if __name__ == "__main__":
    pytest.main([__file__])