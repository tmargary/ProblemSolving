"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs inO(n)time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
    elements of nums except nums[i].

    Ex:
    nums:           [ 1,  2, 3, 4]
    left_array:     [ 1,  1, 2, 6]
    right_array:    [24, 12, 4, 1]
    answer:         [24, 12, 8, 6]
    """

    # Calculate the left array
    left_array = list()
    product = 1
    for val in nums:
        left_array.append(product)
        product *= val

    print(left_array)

    # Calculate the right array
    right_array = list()
    product = 1
    for val in nums[::-1]:
        right_array.append(product)
        product *= val
    right_array.reverse()

    print(right_array)

    # Elementwise multiplication
    answer = [x * y for x, y in zip(left_array, right_array)]

    return answer  #


if __name__ == '__main__':
    # time complexity: O(n)
    # space complexity: O(n)

    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
