def accumulate(lst):
    """
    >>> l = [1, 5, 13, 4]
    >>> accumulate(l)
    23
    >>> l
    [1, 6, 19, 23]
    >>> deep_l = [3, 7, [2, 5, 6], 9]
    >>> accumulate(deep_l)
    32
    >>> deep_l
    [3, 10, [2, 7, 13], 32]
    """
    length = len(lst)
    total = 0
    for i in range(length):
        item = lst[i]
        if isinstance(item,list):
            inside = accumulate(item)
            total += inside
        else:
            lst[i] = total + item
            total += item
    return total

def has_seven(k): # Use this function for your answer below
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def make_pingpong_tracker():
    """ Returns a function that returns the next value in the
    pingpong sequence each time it is called.
    >>> output = []
    >>> x = make_pingpong_tracker()
    >>> for _ in range(9):
    ...     output += [x()]
    >>> output
    [1, 2, 3, 4, 5, 6, 7, 6, 5]
    """
    index, current, add = 0, 0, True
    def pingpong_tracker():
        nonlocal index,current,add
        index+=1
        if add:
            current+=1
        else:
            current-=1
        if has_seven(index):
            add = not add
        return current
    return pingpong_tracker
