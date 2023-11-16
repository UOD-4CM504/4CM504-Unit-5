import exercise_5_1

def test_main(self):
  # Function name you want to check
  function_name_to_check = 'main'

  # Check if the function is defined
  self.assertTrue(function_name_to_check in globals(), msg="main function not defined")

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

    with patch('builtins.input', side_effect=mock_input_func) as mock_input:
      with patch('builtins.print', side_effect=mock_print_func) as mock_print:
        func_success = True
        try:
          main()                                  # Call unchanged function.
        except Exception as e:
          error = f"Main method failed. {e}"
          output.append(error)

    output = "".join(output)
    expected_output = "".join(expected_output)
    self.assertEquals(output, expected_output)

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
