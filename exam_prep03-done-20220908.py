
def sum_range(t):
    def helper(t):
        if is_leaf(t):
            return [label(t),0]
        else:
            a=min([sum_range(b) for b in branches(t)])
            b=max([sum_range(b) for b in branches(t)])
            x=label
    x,y=helper(t)
    return x-y

def helper(t):
    """"
    """
    if is_leaf(t):
        return label(t)
    else:
        return [helper(b)+label(t) for b in branches(t)]

def no_eleven(n):
    if n==0:
        return []
    elif n==1:
        return [[6],[1]]
    else:
        a=no_eleven(n-1)
        result=[]
        for pair in a:
            if pair[-1] == 6:
                result.append(pair+[6])
                result.append(pair+[1])
            else:
                result.append(pair+[6])
        return result


def mul(lst):
    total = 1
    for elem in lst:
        total *= elem
    return total

def eval_with_add(t):
    """Evaluate an expression tree of * and + using only
    addition.
    >>> plus = tree('+', [tree(2), tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = tree('*', [tree(2), tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = tree('*', [tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(tree('*'))
    1
    """
    if label(t) == '+':
        return sum([label(b) for b in branches(t)])
    elif label(t) == '*':
        return mul([eval_with_add(b) for b in branches(t)])
    else:
        return label(t)



def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)
