"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in
nums1.
"""
from typing import List


class SolutionOn2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for n2 in nums2:
            inserted = False
            for i in range(m):
                if n2 <= nums1[i]:
                    nums1.insert(i, n2)
                    nums1.pop()
                    m += 1
                    inserted = True
                    break
            if not inserted:
                nums1.insert(m, n2)
                m += 1
                nums1.pop()

        return None


class SolutionOn:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return None

        sorted_list = list()
        length = m + n

        i, j = 0, 0

        for _ in range(length):
            n1 = nums1[i] if i < m else None
            n2 = nums2[j] if j < n else None
            if n1 is not None and n2 is not None:
                if n1 < n2 and i < m and j < n:
                    sorted_list.append(nums1[i])
                    i += 1
                elif n1 >= n2 and j < n:
                    sorted_list.append(n2)
                    j += 1
            elif n1 is None:
                sorted_list.append(n2)
                j += 1
            elif n2 is None:
                sorted_list.append(n1)
                i += 1

        for i in range(len(nums1)):
            nums1[i] = sorted_list[i]

        return None

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    if n == 0:
        return None

    j = n - 1
    for i in range(len(nums1) - 1, -1, -1):
        if i > m:
            nums1[i] = nums2[j]
            j -= 1
        elif n == 1:
            nums1[i] = nums2[j]
        else:
            if nums2[j] <= nums1[i]:
                nums1[i], nums1[i + 1] = nums2[j], nums1[i]
                j -= 1
    print(nums1)
    return None


if __name__ == '__main__':
    a = [1, 2, 3, 0, 0, 0]
    m = 3
    b = [2, 5, 6]
    n = 3
    merge(a, m, b, n)

    a = [0]
    m = 0
    b = [1]
    n = 1
    merge(a, m, b, n)
