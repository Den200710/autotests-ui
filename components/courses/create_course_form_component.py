from re import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input', 'Title')
        self.estimated_title_input = Input(page, 'create-course-form-estimated-time-input', 'Estimated')
        self.description_textarea = Textarea(page, 'create-course-form-description-input', 'Description')
        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'Max score')
        self.min_score_input = Input(page, 'create-course-form-min-score-input', 'Min score')

    def fill(self, title: str, estimated_title: str, description: str, max_score: str, min_score: str):
        self.title_input.fill(title)
        self.estimated_title_input.fill(estimated_title)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

    def check_visible(self, title: str, estimated_title: str, description: str, max_score: str, min_score: str):
        self.title_input.check_have_value(title)
        self.estimated_title_input.check_have_value(estimated_title)
        self.description_textarea.check_have_value(description)
        self.max_score_input.check_have_value(max_score)
        self.min_score_input.check_have_value(min_score)
