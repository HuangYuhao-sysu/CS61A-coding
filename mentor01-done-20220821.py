def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    if n < 10:
        return True
    else:
        last1, left1 = n%10, n//10
        last2 = left1%10
        if last1 > last2:
            return False
        else:
            return is_sorted(left1)

def mario_number(level):
    """
    Return the number of ways that Mario can traverse the
    level, where Mario can either hop by one digit or two
    digits each turn. A level is defined as being an integer
    with digits where a 1 is something Mario can step on and 0
    is
    something Mario cannot step on.
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """
    last1, left1 = level%10, level//10  # 1001 -> 1, 100
    last2, left2 = left1%10, left1//10  # 100  -> 0, 10
    last3        = left2%10             # 10   -> 0
    if level == 1:
        return 1
    elif (last3, last2) == (0, 0):
        return 0
    elif (last3, last2) == (0, 1):
        return mario_number(left1)
    elif (last3, last2) == (1, 0):
        return mario_number(left2)
    elif (last3, last2) == (1, 1):
        return 2*mario_number(left2)
    else:
        return 0

def make_change(n):
    """Write a function, make_change that takes in an
    integer amount, n, and returns the minimum number
    of coins we can use to make change for that n,
    using 1-cent, 3-cent, and 4-cent coins.
    Look at the doctests for more examples.
    >>> make_change(5)
    2
    >>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3
    2
    """
    if n < 0:
        return 0
    elif n==1 or n==3 or n==4:
        return 1
    elif n==2 or n==5 or n==6:
        return 2
    else:
        return 1 + make_change(n-4)


def elephant_roster(elephants):
    """
    Takes in a list of elephants and returns a list of their
    names.
    """
    return [elephant_name(elephant) for elephant in elephants]

"""def elephant_name(e):
    return e[0][0]
def elephant_age(e):
    return e[0][1]
def elephant_can_fly(e):
    return e[1]"""

def elephant(name, age, can_fly):
    """
    >>> chris = elephant("Chris Martin", 38, False)
    >>> elephant_name(chris)
    "Chris Martin"
    >>> elephant_age(chris)
    38
    >>> elephant_can_fly(chris)
    False
    """
    def select(command):
        if command == "name":
            return name
        elif command == "age":
            return age
        elif command == "can_fly":
            return can_fly
    return select



def elephant_name(e):
    return e("name")
def elephant_age(e):
    return e("age")
def elephant_can_fly(e):
    return e("can_fly")
