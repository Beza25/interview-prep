def find_largest(numbers):
    largest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

def test_find_largest_positive():
    assert find_largest([3, 7, 2]) == 7


def test_find_largest_negative():
    assert find_largest([-5, -2, -9]) == -2


def test_find_largest_first_is_biggest():
    assert find_largest([10, 4, 6]) == 10
