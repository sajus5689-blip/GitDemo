import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_new():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string do not match"

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Test failed because addition fail"