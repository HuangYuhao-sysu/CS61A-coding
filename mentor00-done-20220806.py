
def mystery(f, x):
    """
    >>> from operator import add, mul
    >>> a = mystery(add, 3)
    >>> a(4) # add(3, 4)
    7
    >>> a(12)
    15
    >>> b = mystery(mul, 5)
    >>> b(7) # mul(5, 7)
    35
    >>> b(1)
    5
    >>> c = mystery(lambda x, y: x * x + y, 4)
    >>> c(5)
    21
    >>> c(7)
    23
    """
    return lambda y: f(x, y)

square = lambda x: x*x

foo = mystery(lambda a, b: a(b), lambda c: 5 + square(c))
foo(-2)

def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
        if k == 1:
            return '-' + middle + '-' + end
        else:
            return '-' + middle + repeat(k-1)
    print(start + repeat(num))

(lambda x: lambda y: lambda : y(x))(3)(lambda z: z*z)()



def combine(n, f, result):
    """
    Combine the digits in non-negative integer n using f.
    >>> combine(3, mul, 2) # mul(3, 2)
    6
    >>> combine(43, mul, 2) # mul(4, mul(3, 2))
    24
    >>> combine(6502, add, 3) # add(6, add(5, add(0, add(2, 3)
    )))
    16
    >>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0))))
    8
    """
    """
    if n == 0:
        return result
    else:
        l = len(str(n))
        return f(n // (10**(l-1)), combine(n % (10**(l-1)), f, result))
    """
    if n == 0:
        return result
    else:
        return combine(n // 10, f, f(n % 10, result))


mul = lambda x, y: x*y
add = lambda x, y: x+y




def has_sum(total, n, m):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 0 * 3 + 1 * 5 = 5
    True
    >>> has_sum(11, 3, 5) # 2 * 3 + 1 * 5 = 11
    True
    """"""
    """
    if total == n or total == m:
        return True
    elif total < n and total < m:
        return False
    else:
        return has_sum(total-n, n, m) or has_sum(total-m, n, m)

def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer 1 prints within this range
    True
    >>> sum_range(40, 55) # Printer 1 can print a number 56-60
    False
    >>> sum_range(170, 201) # Printer 1 + 2 will print between
    180 and 200 copies total
    True
    """
    for total in range(lower, upper+1):
        if has_sum(total, 60, 140):
            return True
    return False
