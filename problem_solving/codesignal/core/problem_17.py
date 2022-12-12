def int8_to_binary(n):
    """
    Given an integer n, return its binary representation.
    :param n: integer
    """

    # verify that the number will fit in 1 byte int
    if n > 2**7-1 or n < -2**7:
        raise ValueError(f"Can't store a store a value larger than {2**7-1} or smaller than {-2**7}.")

    n_copy = abs(n)
    binary = ""
    while n_copy > 0:
        binary = binary + str(n_copy % 2)
        n_copy = n_copy // 2

    # append necessary 0's to get the 1 byte binary representation
    binary = binary + '0' * (8 - len(binary))
    binary = binary[::-1]

    # if the number is positive or 0
    if n >= 0:
        return binary
    # if the number is negative
    else:
        return '1' + binary[1:]


def binary_to_int8(string):
    """
    Given a binary representation of an int, return its integer representation.
    :param string: binary number
    """
    # get the integer
    integer = 0
    degree = len(string) - 1
    for i, bit in enumerate(string[1:]):
        integer += 2 ** (degree - i-1) * int(bit)

    # add the negative sign if necessary
    if string[0] == '1':
        integer = -integer
    return integer


def decipher(n, k):
    """
    Return the deciphered n by changing the 1 to 0 at the k'th position
    :param n:
    :param k:
    :return:
    """
    # from int to binary
    binary = int8_to_binary(n)
    # change the bit
    binary = binary[:-k] + '0' + binary[-k + 1:]
    # ignore bits if necessary (when k is 1)
    binary = binary[:8]
    # from binary back to int and return
    return binary_to_int8(binary)


def main():
    # test cases
    cases = {
        (37, 3): 33,
        (-37, 3): -33,
        (37, 4): 37,
        (-37, 4): -37,
        (0, 3): 0,
        (1, 1): 0,
    }

    for args, expected in cases.items():
        result = decipher(*args)
        if result != expected:
            print(f'Test case {args} = {expected} failed! result = {result}')


if __name__ == '__main__':
    main()
