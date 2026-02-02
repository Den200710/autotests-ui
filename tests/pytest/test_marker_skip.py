import pytest

@pytest.mark.skip(reason='Пропуск')
def test_skip():
    print('skip')

VERSION = "v.1.3.0"

@pytest.mark.skipif(
    VERSION == "v.1.3.0",
    reason='Пропуск из-за условий')
def test_skip_if():
    print('skip_if')