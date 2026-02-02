import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1,1), (2,4), (3,9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os+browser) > 0


@pytest.fixture(params=['chromium', 'firefox'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print((f'Running test on browser: {browser}'))

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operation(self, user: str, account: str):
        ...

    def test_user_without_operation(self, user: str):
        ...

users = {
    '+79000000000': 'User with money',
    '+79000000001': 'User without money',
    '+79000000002': 'User with operation',
}

@pytest.mark.parametrize(
    'number',
    users.keys(),
    ids= lambda number: f'{number}: {users[number]}'
)
def test_identifires(number: str):
    ...
