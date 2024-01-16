# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    dict1 = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in dict1:
            return [dict1[complement], i]
        dict1[nums[i]] = i

    return []  # No solution found


print(two_sum([1, 2, 3, 4], 5))
