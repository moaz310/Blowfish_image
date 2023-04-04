import math


def freq_monobit_test(data):
    """Perform a frequency (monobit) test on binary data."""
    newdata = [int(x) for x in data]
    n = len(newdata)
    ones = sum(newdata)
    zeros = n - ones
    s = abs(ones - zeros)
    p_value = math.erfc(s / math.sqrt(2*n))
    return p_value


if __name__ == '__main__':

    print(freq_monobit_test('110010010000111111011010101000100010000101101000'
                            '1100001000110100110001001100011001100010100010111000'))
