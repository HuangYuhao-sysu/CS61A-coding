HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a)-street(b)) + abs(avenue(a)-avenue(b))


def is_squares(num):
    """If num is a total square number, then return True

    >>> is_squares(9)
    True
    >>> is_squares(15)
    False
    >>> is_squares(1)
    True
    """
    for i in range(0,num+1):
        if i*i == num:
            return True
    return False

def get_sqrt(num):
    """Get the number's sqrt number

    >>> get_sqrt(100)
    10
    >>> get_sqrt(9)
    3
    >>> get_sqrt(7)
    """
    if is_squares(num):
        for i in range(0,num+1):
            if i*i == num:
                return i
    else:
        return None

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    return [get_sqrt(num) for num in s if is_squares(num)]



def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    curr = 0
    p1 = 1
    p2 = 2
    p3 = 3
    if n <= 3:
        return n
    else:
        for _ in range(n-3):
            curr = p3 + 2*p2 + 3*p1
            p3, p2, p1 = curr, p3, p2
        return curr

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    """i = 1
    curr_pingpong = 1
    dir = 0 # add == 0, sub == 1
    while i < n:
        if chg_dir(i):
            dir = ~dir
        curr_pingpong = nxt_pingpong(curr_pingpong, dir)
        i += 1
    return curr_pingpong"""
    if n <= 3:
        return n
    else:
        if chg_dir(n-1):
            return pingpong(n-2)
        else:
            return 2*pingpong(n-1) - pingpong(n-2)

def chg_dir(num):
    """Return if the num is a multiply of 7 or contains digit 7

    >>> chg_dir(1)
    False
    >>> chg_dir(7)
    True
    >>> chg_dir(14)
    True
    >>> chg_dir(17)
    True
    >>> chg_dir(28)
    True
    """
    if num % 7 == 0:
        return True
    elif has_digit_seven(num):
        return True
    else:
        return False

def has_digit_seven(num):
    """Return True if num has digit 7

    >>> has_digit_seven(17)
    True
    >>> has_digit_seven(24)
    False
    >>> has_digit_seven(157846)
    True
    """
    if num < 10:
        return num == 7
    else:
        left, last = num // 10, num % 10
        if last == 7:
            return True
        else:
            return has_digit_seven(left)

def nxt_pingpong(curr_pingpong, dir):
    """Return next pingpong number, add when dir == 0, sub when dir == 1

    >>> nxt_pingpong(4,0)
    5
    >>> nxt_pingpong(8,1)
    7
    """
    if dir:
        return curr_pingpong - 1
    else:
        return curr_pingpong + 1

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    pow_of_2 = 1
    while pow_of_2 < amount:
        pow_of_2 *= 2
    return count_patition(amount, pow_of_2)

def count_patition(amount,num):
    """Return the number of ways to make change for amount, num is the pow of 2

    >>> count_patition(7, 4)
    6
    >>> count_patition(10,8)
    14
    >>> count_patition(20,16)
    60
    >>> count_patition(100,64)
    9828
    """
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif num == 1:
        return 1
    else:
        with_num = count_patition(amount-num,num)
        without_num = count_patition(amount, int(num/2))
        return with_num + without_num

###################
# Extra Questions #
###################

from operator import sub, mul

fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k:f(f,k)) (lambda f, k: 1 if k==1 else mul(k, f(f,sub(k,1)) ))






