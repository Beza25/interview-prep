"""
Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.
Example:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The subarray with the maximum sum is [5, 1, 3] with a sum of 9.

"""


def sliding_window(nums, k):

    result = float("-inf")
    start, current_sum = 0, 0

    for end in range(len(nums)):
        current_sum += nums[end]

        if end - start + 1 == k:
            result = max(result, current_sum)
            current_sum -= nums[start]
            start += 1

    return result


"""
    Write a function to calculate the maximum number of fruits you can collect from an integer array fruits,
    where each element represents a type of fruit. You can start collecting fruits from any position in the array, 
    but you must stop once you encounter a third distinct type of fruit. The goal is to find the longest subarray 
    where at most two different types of fruits are collected.
    Example:
    Input: fruits = [3, 3, 2, 1, 2, 1, 0]
    Output: 4
    Explanation: We can pick up 4 fruit from the subarray [2, 1, 2, 1]
"""


def max_sum_of_subarr(fruits, k):
    # - distinct = 0
    # - result = 0
    # - start = 0
    # - loop over elements with end
    # - check if it is the same as previous if so  (add 1 to distinct and add to 1 result ) go to next
    # - else: check if distinct is

    # start =  0, 0, 0
    # end =    1, 2, 3
    # count =  2, 3, 3
    # dist =   1, 2, 3
    # result = 1, 3

    #  for i in range(len(nums) - 1, start + 1, -1):
    if fruits.len() == 1:
        return 1
    if fruits.len() == 0:
        return 0
    start, distinct, result, current_count = 0, 0, 1, 1, 1

    # for i in range(len(nums) - 1, start + 1, -1):

    for end in range(1, len(fruits) - 1, +1):
        if fruits[end] != fruits[end - 1] and distinct < k - 1:
            distinct += 1
            current_count += 1
            result = current_count
        elif fruits[end] != fruits[end - 1] and distinct == k - 1:
            result = max(result, current_count)
            start += end - 1
            distinct -= 1
            current_count = 0
        current_count += 1

    if result == 1:
        return current_count
    return result
