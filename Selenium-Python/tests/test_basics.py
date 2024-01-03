import pytest

@pytest.mark.add
def test_add():
    a = 2
    b = 3
    c = 5
    temp = a + b
    assert c == temp
@pytest.mark.demo
def test_demo1():
    assert True
@pytest.mark.qa
def test_QA():
    assert False
