import math
import pytest
from calc import add, subtract, std


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-2, -3) == 1


def test_std_basic():
    # Standard deviation of [1, 2, 3, 4, 5]
    # mean = 3, variance = (4+1+0+1+4)/5 = 2, std = sqrt(2)
    assert std([1, 2, 3, 4, 5]) == pytest.approx(math.sqrt(2))


def test_std_single_element():
    # Standard deviation of a single element is 0
    assert std([5]) == 0.0
    assert std([0]) == 0.0
    assert std([-3]) == 0.0


def test_std_identical_elements():
    # Standard deviation of identical elements is 0
    assert std([7, 7, 7, 7]) == 0.0


def test_std_negative_numbers():
    # Standard deviation of [-2, -1, 0, 1, 2]
    # mean = 0, variance = (4+1+0+1+4)/5 = 2, std = sqrt(2)
    assert std([-2, -1, 0, 1, 2]) == pytest.approx(math.sqrt(2))


def test_std_floats():
    assert std([1.5, 2.5, 3.5]) == pytest.approx(math.sqrt(2/3))


def test_std_empty_list_raises():
    with pytest.raises(ValueError):
        std([])


def test_std_two_elements():
    # Standard deviation of [1, 3]
    # mean = 2, variance = (1+1)/2 = 1, std = 1
    assert std([1, 3]) == 1.0


def test_std_population_not_sample():
    # Verify we use population std (N) not sample std (N-1)
    # For [1, 2, 3]: population std = sqrt(2/3), sample std = sqrt(1)
    assert std([1, 2, 3]) == pytest.approx(math.sqrt(2/3))