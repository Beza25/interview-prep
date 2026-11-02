from collections import defaultdict


def two_sum(nums, target):
    # Return indices of the two numbers that add up to target in sorted array
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return left, right
    return (0, 0)


"""
    Given an input integer array nums (not necessarily sorted), 
    write a function to find all unique triplets
    [nums[i], nums[j], nums[k]] such that i, j, and k are distinct indices, 
    and the sum of nums[i], nums[j], and nums[k] equals zero. 
    Ensure that the resulting list does not contain any duplicate triplets.

    Input: nums = [ -1, 0, 1, 2, -1, -1 ]
    Output:[ [ -1, -1, 2 ],[ -1, 0, 1 ] ]
"""


def three_sum(nums):

    nums.sort()

    if nums[len(nums) - 1] < 0:
        return []

    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right += 1
                left += 1
                right -= 1

    return result
