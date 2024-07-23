import pytest
import inspect
import io
import sys
from unittest.mock import patch
from l4_KeywordArgumentsAndDefaultValues import print_list

def test_function_exists():
    function_name = "print_list"
    assert function_name in globals(), f"{function_name} is not defined"

def test_function_arguments():
    argspec = inspect.getfullargspec(print_list)
    arguments = argspec.args[:len(argspec.args) - len(argspec.defaults)] if argspec.defaults else argspec.args
    assert len(arguments) == 1, "Function does not take in a single positional argument"

    keyword_arguments = argspec.args[-len(argspec.defaults):] if argspec.defaults else []
    assert "multiple" in keyword_arguments, "Function does not have a keyword argument called multiple"

    assert argspec.defaults[-1] == 1, "Default value for 'multiple' should be 1"

@pytest.mark.parametrize("input_list, multiple, expected_output", [
    ([4, 3, 2, 1], None, "4\n3\n2\n1\n"),
    ([2, 3, 6, 4], 2, "4\n6\n12\n8\n"),
    ([2, 3, 6, 4], 3, "6\n9\n18\n12\n"),
    ([2, 3, 6, 4], 5, "10\n15\n30\n20\n")
])
def test_print_list_output(input_list, multiple, expected_output):
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        if multiple is None:
            print_list(input_list)
        else:
            print_list(input_list, multiple=multiple)
        assert fake_out.getvalue() == expected_output, f"Failed when using multiple={multiple}"

def test_print_list_default_behavior():
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        print_list([4, 1, 6, 7])
        assert fake_out.getvalue() == "4\n1\n6\n7\n", "Failed with default multiple value"