#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
# -k stands for methods name execution, -s logs in output, -v more info metadata
# you can run specific file with py.test <file name>
# you can mark (tag) @pytest.mark.smoke and then rum with -m
# you can skip test with @pytest.mark.skip
#@pytest.mark.xfail - used for any failure testcases
# fixtures are used as setup and tear down methods for test cases - conftest file to generalize fixture and make it available to all test cases
#datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")



@pytest.mark.skip
def test_SecondGreeterCreditCard():
    print("GoodMorning")

#@pytest.mark.usefixtures("crossBrowser")
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])