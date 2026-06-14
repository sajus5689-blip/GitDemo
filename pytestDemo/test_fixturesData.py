import pytest


@pytest.mark.usefixtures("DataLoad")
class TestExample2:
    def test_editProfile(self, DataLoad):
        print(DataLoad[0])