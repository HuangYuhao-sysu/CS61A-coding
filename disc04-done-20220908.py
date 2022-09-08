
def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def fn(f):
        nonlocal n
        n = f(n)
        print(n)
        return memory(n)
    return fn


def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    times_lst = [i for i in lst if i==x]
    times=len(times_lst)
    for _ in range(times):
        lst.append(el)

def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    l = len(lst)
    if l%2==0:
        for i in range(l/2):
            lst[i],lst[l-1-i] = lst[l-1-i],lst[i]
    else:
        for i in range(int((l-1)/2)):
            lst[i],lst[l-1-i] = lst[l-1-i],lst[i]

def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> dir = group_by(range(-3, 4), lambda x: x * x)
    >>> {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]} == dir
    True
    """
    dir = {}
    dir = {fn(i):[] for i in s}
    for x in s:
        dir[fn(x)].append(x)
    return dir

def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, 'x', 'y')
    >>> d
    {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    """
    for key in d:
        if type(d[key]) != dict:
            if d[key] == x:
                d[key] = y
        else:
            replace_all_deep(d[key],x,y)


