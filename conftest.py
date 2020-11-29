import pytest

@pytest.fixture(scope='class')
def comment_calc():
    print('开始计算')
    yield
    print('结束计算')



