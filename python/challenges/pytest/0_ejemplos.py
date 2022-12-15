# pytest
# content of test_sample.py
def my_fun(x):
    return x + 1


def test_my_fun():
    assert my_fun(3) == 4

def fun():
    return True

def test_fun():
    assert fun() == True