
def solution(x):
    """
    Count the number of 1 bits
    """
    cnt = 0
    x = abs(x)  # because in Python, -1 is '-0b1'. Check with bin(-1)
    while x != 0:
        if x & 1 == 1:  # if number is odd, meaning the 1 bit is at the first position, ready for removal
            cnt += 1
        x = x >> 1

    return cnt


if __name__ == '__main__':
    # Time complexity: O(n)
    # Space complexity: O(1)
    assert solution(0) == 0
    assert solution(1) == 1
    assert solution(37) == 3
