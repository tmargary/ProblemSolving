"""
Count the number of 1 bits
"""


def solution(x):
    cnt = 0
    while x != 0:
        if x & 1 == 1:  # if number is even
            cnt += 1
        x = x >> 1

    return cnt


if __name__ == '__main__':
    assert solution(0) == 0
    assert solution(1) == 1
    assert solution(37) == 3
