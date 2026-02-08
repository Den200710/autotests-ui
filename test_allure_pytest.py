import allure


def test_feature(title: str):
    with allure.step("Шаг 1"):
        ...

    with allure.step(f'Step 2{title}'):
        ...


@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    pass


def test_feature_11():
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwright")