import allure
from allure_commons.types import Severity

from tools.routes import AppRoute
import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStory
from config import settings


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
class TestRegistration:
    @pytest.mark.xdist_group(name="authorization-group")
    @allure.title('Correct registration')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.fill_registration_form.fill(email=settings.test_user.email,
                                                      username=settings.test_user.username,
                                                      password=settings.test_user.password)
        registration_page.fill_registration_form.check_visible(email=settings.test_user.email,
                                                               username=settings.test_user.username,
                                                               password=settings.test_user.password)
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view_component.check_visible()
