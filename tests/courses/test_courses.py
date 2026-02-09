import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStory
from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empy courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title('Check correct create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        create_course_page.visit(AppRoute.CREATE_COURSES)

        create_course_page.crete_course_toolbar_view_component.check_visible()
        create_course_page.crete_course_toolbar_view_component.check_disabled_create_course_button()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form_component.check_visible(title="",
                                                                      max_score="0",
                                                                      min_score="0",
                                                                      description="",
                                                                      estimated_title="")
        create_course_page.create_course_toolbar_view_component.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form_component.fill(title="Playwright",
                                                             estimated_title="2 weeks",
                                                             description="Playwright",
                                                             max_score="100",
                                                             min_score="10")
        create_course_page.crete_course_toolbar_view_component.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0,
                                                    title="Playwright",
                                                    max_score="100",
                                                    min_score="10",
                                                    estimated_time="2 weeks")

    @allure.title('Check edit courses list')
    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):

        create_course_page.visit(AppRoute.CREATE_COURSES)

        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form_component.fill(title="Playwright",
                                                             estimated_title="2 weeks",
                                                             description="Playwright",
                                                             max_score="100",
                                                             min_score="10")
        create_course_page.crete_course_toolbar_view_component.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0,
                                                    title="Playwright",
                                                    max_score="100",
                                                    min_score="10",
                                                    estimated_time="2 weeks")
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form_component.fill(title="Playwright Edit",
                                                             estimated_title="3 weeks",
                                                             description="Playwright Edit",
                                                             max_score="1000",
                                                             min_score="100")
        create_course_page.crete_course_toolbar_view_component.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0,
                                                    title="Playwright Edit",
                                                    max_score="1000",
                                                    min_score="100",
                                                    estimated_time="3 weeks")

