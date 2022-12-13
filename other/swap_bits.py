

def solution(n, i, j):
    """
    swap the i'th and the j'th bits of the number n
    :param n: int number
    :param i: index 1
    :param j: index 2
    """

    a = n >> i
    b = n >> j

    a = a & 1
    b = b & 1

    tmp = a << i | b << j

    result = n ^ tmp

    return result


if __name__ == '__main__':
    assert solution(37, i=2, j=6) == 33  # 00100101 -> 00100001
