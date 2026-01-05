import pytest


@pytest.mark.xfail(reason='Есть баг, но не пропускаем, знаем о нем')
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason='Баг исправлен, тест прошел успешно')
def test_without_bug():
    assert 1 == 1