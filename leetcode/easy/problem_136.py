"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

"""
from typing import List


def singleNumber(nums: List[int]) -> int:
    d = dict()

    for el in nums:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1

    for el, val in d.items():
        if val == 1:
            return el


if __name__ == '__main__':
    assert singleNumber([2, 2, 1]) == 1
    assert singleNumber([1]) == 1
