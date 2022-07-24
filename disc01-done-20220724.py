
"""1.3"""

square = lambda x: x * x

def so_slow(num):
    x = num
    while x > 0:
        x += 1
    return x / 0

def is_prime(n):
    for div in range(2, n):
        if n % div == 0:
            return False
    return True

def is_even(x):
    return x % 2 == 0

def keep_ints(cond, n):
    for num in range(1, 5):
        if cond(num):
            print(num)

def outer(n):
    def inner(m):
        return n -m
    return inner

def keep_ints_new(n):
    def cond(f):
        for num in range(1, n):
            if f(num):
                print(num)
    return cond



from operator import add
def sub(a, b):
    sub = add
    return a -b
add = sub
sub = min
print(add(2, sub(2, 3)))
