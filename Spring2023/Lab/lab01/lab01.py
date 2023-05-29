def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        return 1
    sum = n
    for i in range(k - 1):
        n = n - 1
        sum = sum * n
    return sum


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    count = 0
    for i in range(n + 1):
        if i == 0:
            pass
        elif i % k == 0:
            print(i)
            count = count + 1
    return count



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    count = 0
    sum = 0
    number = y
    while(y):
        count = count + 1
        y = y / 10

    for i in range(count - 1):
        sum = sum + int(number) % 10
        number = int(number) / 10
    return sum
        


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    length = 0
    count = 0
    number = n
    while(n):
        length = length + 1
        n = int(n / 10)

    if length <= 1:
        return False

    for i in range(length):
        single_number = number % 10
        if single_number == 8:
            update_number = int(number / 10)
            next_number = update_number % 10
            if next_number == 8:
                return True
            count = count + 1
        number = int(number / 10)

    if count < 2:
        return False

    return False