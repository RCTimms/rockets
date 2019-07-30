import numpy as np


def test_one_plus_one_is_two():
    "Check that one and one are indeed two."
    assert 1 + 1 == 2, "No, you're wrong!"

def test_something_random():
    np.random.seed(1)
    a = np.random.randn()
    assert a == 1.6243453636632417, "It's random!"
    