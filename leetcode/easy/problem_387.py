"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


def firstUniqChar(s: str) -> int:
    d = dict()

    for i, ch in enumerate(s):
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    for idx, ch in enumerate(s):
        if d[ch] == 1:
            return idx
    return -1


if __name__ == '__main__':
    # Time complexity: O(n)
    # Space complexity: O(n)
    assert firstUniqChar("leetcode") == 0
    assert firstUniqChar("loveleetcode") == 2
    assert firstUniqChar("aabb") == -1
