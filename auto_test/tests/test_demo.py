import pytest

@pytest.fixture()
def before_after():    
    print("before")
    yield
    print("\nafter")

def test_demo():
    assert 1 + 1 == 2

def test_demo2(before_after):
    assert 2 * 2 == 4