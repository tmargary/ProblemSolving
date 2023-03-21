"""
Count whether the number of 1 bits is odd or even
"""

def solution(x):
    cnt = 0
    x = abs(x)  # because in Python, -1 is '-0b1'. Check with bin(-1)
    while x != 0:
        if x & 1 == 1:  # if number is odd, meaning the 1 bit is at the first position, ready for removal
            cnt += 1
        x = x >> 1

    if cnt & 1 == 1:
        return 'odd'
    elif cnt == 0:
        return 'none'
    else:
        return 'even'


if __name__ == '__main__':
    # Time complexity: O(n)
    # Space complexity: O(1)
    assert solution(0) == 'none'
    assert solution(1) == 'odd'
    assert solution(3) == 'even'
    assert solution(37) == 'odd'
