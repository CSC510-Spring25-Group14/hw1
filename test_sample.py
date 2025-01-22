import pytest
from myfile import factorial

def test_factorial_1():
    assert factorial(0) == 1

def test_factorial_2():
    assert factorial(6) == 720

def test_factorial_3():
    with pytest.raises(ValueError, match="Factorial is defined only for positive integers."):
        factorial(-5)

def test_factorial_4():
    assert factorial(5) == 100 #factorial(5) is 120, not 100
