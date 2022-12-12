def int_to_binary(n):
    """
    Given an integer n, return its binary representation.
    :param n: integer
    """
    binary = ""
    if n >= 0:
        while n > 0:
            binary = binary + str(n % 2)
            n = n // 2
    else:
        raise NotImplementedError(f"I don't know how to get the binary representation of {n}.")
    binary = binary + '0' * (8 - len(binary))
    binary = binary[::-1]
    return binary


def binary_to_int(string):
    """
    Given a binary representation of an int, return its integer representation.
    :param string: binary number
    """
    integer = 0
    degree = len(string) - 1
    for i, bit in enumerate(string):
        integer += 2 ** (degree - i) * int(bit)
    return integer


def decipher(n, k):
    """
    Return the deciphered n by changing the 1 to 0 at the k'th position
    :param n:
    :param k:
    :return:
    """
    binary = int_to_binary(n)
    binary = binary[:-k] + '0' + binary[-k+1:]
    return binary_to_int(binary)


def main():
    assert decipher(37, 3) == 33
    assert decipher(37, 4) == 37


if __name__ == '__main__':
    main()
