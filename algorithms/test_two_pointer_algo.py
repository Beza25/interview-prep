import pytest

from algorithms.two_pointer_algo import three_sum, two_sum

NOT_FOUND = (0, 0)


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 4, 5, 8, 10, 13], 13, (1, 5)),  # typical case
        ([1, 2], 3, (0, 1)),  # smallest valid input
        ([1, 3, 5, 7, 9], 10, (0, 4)),  # pair at both ends
        ([2, 2], 4, (0, 1)),  # duplicate values
        ([-5, -3, 0, 2, 4], -8, (0, 1)),  # negatives
    ],
)
def test_two_sum_found(nums, target, expected):
    assert two_sum(nums, target) == expected


@pytest.mark.parametrize(
    "nums, target",
    [
        ([], 5),  # empty list
        ([5], 10),  # single element
        ([1, 3, 4, 6], 6),  # only 3 + 3 works, which reuses an index
        ([1, 3, 5], 100),  # target out of range
    ],
)
def test_two_sum_not_found(nums, target):
    assert two_sum(nums, target) == NOT_FOUND


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -1], [[-1, -1, 2], [-1, 0, 1]]),  # typical case
        ([-1, 0, 1], [[-1, 0, 1]]),  # exactly three numbers
        ([3, -2, 1, 0, -1], [[-2, -1, 3], [-1, 0, 1]]),  # unsorted input
        ([0, 0, 0, 0], [[0, 0, 0]]),  # all zeros, one unique triplet
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),  # duplicates on both sides
        (
            [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
        ),  # many triplets with heavy duplication
    ],
)
def test_three_sum_found(nums, expected):
    assert three_sum(nums) == expected


@pytest.mark.parametrize(
    "nums",
    [
        [],  # empty list
        [0, 0],  # fewer than three numbers
        [1, 2, 3],  # all positive
        [-3, -2, -1],  # all negative
        [-1, 0, 2],  # three numbers that don't sum to zero
    ],
)
def test_three_sum_not_found(nums):
    assert three_sum(nums) == []
