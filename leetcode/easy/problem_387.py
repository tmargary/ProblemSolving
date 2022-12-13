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

    non_rep_char = None
    for el, val in d.items():
        if val <= 1:
            non_rep_char = el
            break

    for i, ch in enumerate(s):
        if ch == non_rep_char:
            return i
    return -1


if __name__ == '__main__':
    assert firstUniqChar("leetcode") == 0
    assert firstUniqChar("loveleetcode") == 2
    assert firstUniqChar("aabb") == -1
