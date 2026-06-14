import pytest

def test_login(browserInstance):
    browserInstance.get("https://rahulshettyacademy.com/loginpagePractise/")
    assert "Login" in browserInstance.title