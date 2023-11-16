from exercise_5_1 import *
import timeout_decorator

def test_main(mocker):
  # Function name you want to check
  function_name_to_check = 'main'

  # Check if the function is defined
  assert function_name_to_check in globals(), "main function not defined"

  @timeout_decorator.timeout(1.001)
  def test(test_values, expected_output):
    input_values = test_values
    output = []

    def mock_input_func(*args):
      if len(args) > 0:
        output.append(args[0])
      return input_values.pop(0)
    def mock_print_func(*args, end="\n"):
      temp_str = ""
      if len(args) > 0:
          temp_str = " ".join([str(x) for x in args])
      output.append(f"{temp_str}{end}")

    with mocker.patch('builtins.input', side_effect=mock_input_func), \
     mocker.patch('builtins.print', side_effect=mock_print_func):
        func_success = True
        try:
          main()                                  # Call unchanged function.
        except Exception as e:
          error = f"Main method failed. {e}"
          output.append(error)

    output = "".join(output)
    expected_output = "".join(expected_output)
    assert output, expected_output

  # run first test
  test(['10', '36'], [
        'Please enter a wholesale cost:\n',
        'Please enter a markup percentage:\n',
        f"The retail price is £{13.60:.2f}.\n"
        ])
  # run second test
  test(['100', '52.3'],[
        'Please enter a wholesale cost:\n',
        'Please enter a markup percentage:\n',
        f"The retail price is £{152.30:.2f}.\n"
        ])

def test_calc_retail_price():
  assert calc_retail_price(5,40) == 7.0
  assert round(calc_retail_price(25.3,75),3) == 44.275
