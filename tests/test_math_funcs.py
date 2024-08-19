import pytest
from datetime import datetime
from modules.math_funcs import MathFuncs

# Instantiate the MathFuncs class for testing
math_funcs = MathFuncs()

def test_calculate_mean_average():
    assert math_funcs.calculate_mean_average([1, 2, 3, 4, 5]) == 3.0
    assert math_funcs.calculate_mean_average([10, 20, 30]) == 20.0
    assert math_funcs.calculate_mean_average([-1, -2, -3, -4]) == -2.5
    # Could Add Null Test Here to check if it raises an error. Would Require a Try/Except Block within the Function

def test_calculate_mode_average():
    assert math_funcs.calculate_mode_average([1, 2, 2, 3, 4]) == 2
    assert math_funcs.calculate_mode_average([10, 20, 20, 30, 30, 30]) == 30
    assert math_funcs.calculate_mode_average([5, 5, 5, 5]) == 5
    # Could Add Null Test Here to check if it raises an error. Would Require a Try/Except Block within the Function

def test_round_cordinates():
    assert math_funcs.round_cordinates(54.6789) == 54.68
    assert math_funcs.round_cordinates(-5.93456) == -5.93
    assert math_funcs.round_cordinates(0.5555) == 0.56
    # Could Add Null Test Here to check if it raises an error. Would Require a Try/Except Block within the Function

def test_convert_epoch_to_date():
    assert math_funcs.convert_epoch_to_date(1724005090) == "2024-08-18"
    assert math_funcs.convert_epoch_to_date(1609459200) == "2021-01-01"
    # Could Add Null Test Here to check if it raises an error. Would Require a Try/Except Block within the Function


def test_calculate_median_average():
    # Function is not implemented yet. 
    pass
