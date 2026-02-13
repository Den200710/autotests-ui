import pytest
from allure_commons.types import Severity

from config import settings
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStory
from tools.routes import AppRoute

creds = {
    ("user.name@gmail.com", "password"): 'Invalid email and password',
    ("user.name@gmail.com", " "): 'Empty password',
    (" ", "password"): 'Empty email'
}


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('Correct navigation')
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.fill_registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.fill_login_form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()

    @pytest.mark.xdist_group(name="authorization-group")
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('User login with wrong email or password')
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize('email, password',
                             creds.keys(),
                             ids=creds.values())
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        # allure.dynamic.title(f'User login with wrong email or password: {password}')
        login_page.visit(AppRoute.LOGIN)
        login_page.fill_login_form.fill(email=email, password=password)
        login_page.fill_login_form.check_visible(email=email, password=password)
        login_page.click_login_button()
        login_page.check_wrong_email_or_password_alert()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title('Navigation from login page to registration page')
    @allure.severity(Severity.NORMAL)
    def test_navigation_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()

        registration_page.fill_registration_form.check_visible(email='', username='', password='')

