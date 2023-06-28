def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    pre_num = x % 10
    flag = True
    while x > 0 and flag:
        curr_num = x % 10
        if pre_num < curr_num:
            flag = False
        pre_num = curr_num
        x //= 10
    return flag


ordered_digits(127)