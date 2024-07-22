from exercise_2 import convert_temp
def test_temperature_conversion():
    # Celsius to Fahrenheit cases
    c_to_f_cases = [4, 72, 53, 21, -280, -180]
    c_to_f_answers = [39.2, 161.6, 127.4, 69.8, None, -292.0]

    # Fahrenheit to Celsius cases
    f_to_c_cases = [44, 200, 130, 100.2, -460, -110]
    f_to_c_answers = [6.67, 93.33, 54.44, 37.89, None, -78.89]

    # Test Celsius to Fahrenheit conversion
    for temp_c, expected_f in zip(c_to_f_cases, c_to_f_answers):
        result = convert_temp(temp_c)
        if result is not None:
            result = round(result, 2)
        assert result == expected_f, f"C to F: Expected {expected_f} for {temp_c}°C, but got {result}"

    # Test Fahrenheit to Celsius conversion
    for temp_f, expected_c in zip(f_to_c_cases, f_to_c_answers):
        result = convert_temp(temp_f, Fahrenheit=True)
        if result is not None:
            result = round(result, 2)
        assert result == expected_c, f"F to C: Expected {expected_c} for {temp_f}°F, but got {result}"