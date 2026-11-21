import pytest
from sliding_window import sliding_window


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([2, 1, 5, 1, 3, 2], 3, 9),  # typical case
        ([5, 1, 1, 1, 1], 2, 6),  # best window at the start
        ([1, 1, 1, 3, 2, 4], 3, 9),  # best window at the end
        ([4, 2, 1, 3], 4, 10),  # k == len(nums), one window
        ([3, 7, 2, 5], 1, 7),  # k == 1, just the max element
        ([7], 1, 7),  # single element
        ([-3, -1, -2, -5], 2, -3),  # all negatives
        ([2, -8, 3, -2, 4, -10], 3, 5),  # mixed signs
        ([0, 0, 0, 0], 2, 0),  # all zeros
        ([4, 4, 4, 4, 4], 3, 12),  # every window has the same sum
    ],
)
def test_sliding_window(nums, k, expected):
    assert sliding_window(nums, k) == expected
