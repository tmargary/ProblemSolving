"""
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.


Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

"""
from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    """
    Return the single element that appears only once.
    """
    length = len(nums)

    if length == 1:
        return nums[0]

    if length & 1 == 1:
        nums.append(None)

    length = len(nums)

    window = range(0, length + 1, 2)
    for curr, next in zip(window, window[1:]):
        if curr + 1 > length:
            return nums[-2]
        if nums[curr] != nums[curr + 1]:
            return nums[curr]


if __name__ == '__main__':
    # Time complexity: O(nlog(n))
    # Space complexity: O(1)

    nums = [1, 1, 2]
    assert singleNonDuplicate(nums) == 2

    nums = [1, 1, 2, 3, 3]
    assert singleNonDuplicate(nums) == 2
