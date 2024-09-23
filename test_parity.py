from parity import is_even

def test_parity():
    assert is_even(2) == True
    assert is_even(0) == True
    assert is_even(1) == False
    assert is_even(-2) == True
    assert is_even(-5) == False
