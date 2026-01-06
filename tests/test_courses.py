
from playwright.sync_api import expect

# @pytest.mark.chromium_page_with_state
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    courses_value = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_value).to_be_visible()
    expect(courses_value).to_have_text('There is no results')

    courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    courses_value_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_value_description).to_be_visible()
    expect(courses_value_description).to_have_text('Results from the load test pipeline will be displayed here')