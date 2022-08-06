""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def input_cycle(c):
        def input_value(x):
            if c == 0:
                return x
            elif c == 1:
                return f1(x)
            elif c % 3 == 1:
                return f1(input_cycle(c-1)(x))
            elif c % 3 == 2:
                return f2(input_cycle(c-1)(x))
            elif c % 3 == 0:
                return f3(input_cycle(c-1)(x))
        return input_value
    return input_cycle

## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x % 10 + y * 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return odd_term(n)
    else:
        return term(n, odd_term, even_term) + interleaved_sum(n-1, odd_term, even_term)

def term(n, odd_term, even_term):
    if n % 2 == 0:
        return even_term(n)
    else:
        return odd_term(n)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        left, last = n // 10, n % 10
        ten_paris_of_last_appear_times = appear_times(left)(10-last)
        return ten_paris_of_last_appear_times + ten_pairs(left)


def appear_times(n):
    """Return a function takes m and return how many times m repeats in n

    >>> which_number = appear_times(7823952)
    >>> which_number(2)
    2
    >>> which_number(7)
    1
    """
    def what_number(m):
        if n < 10:
            if n == m:
                return 1
            else:
                return 0
        else:
            left, last = n // 10, n % 10
            if last == m:
                return 1 + appear_times(left)(m)
            else:
                return appear_times(left)(m)
    return what_number
