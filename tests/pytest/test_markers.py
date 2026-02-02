import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.smoke
def test_smoke():
    print('smoke')


@pytest.mark.smoke
@pytest.mark.regression
def test_regress():
    print('smoke')


class TestSuite:
    def test_case1(self):
        print('case1')

    def test_case2(self):
        print('case2')


@pytest.mark.regression
class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass
