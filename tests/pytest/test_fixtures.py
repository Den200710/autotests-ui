import pytest

@pytest.fixture(autouse=True) # Автоматически запускается перед каждым тестом
def send_analytics_data():
    print("[Autouse] Отправляем данные в сервис аналитики")

@pytest.fixture(scope="session") # Запускается один раз на всю тестовую сессию
def settings():
    print("[Session] Инициализируем настройки автотестов")

@pytest.fixture(scope="class") # Запускается один раз на тестовый класс
def user():
    print("[Class] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function") # Запускается по дефолту, можно не указывать
def browser():
    print("[Function] открываем браузер на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...

