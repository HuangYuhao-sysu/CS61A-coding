

def about_equal(t1, t2):
    """Returns whether two trees are 'about equal.'
    Two trees are about equal if and only if they contain
    the same labels the same number of times.
    >> x = tree(1, [tree(2), tree(2), tree(3)])
    >> y = tree(3, [tree(2), tree(1), tree(2)])
    >> about_equal(x, y)
    True
    >> z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    >> about_equal(x, z)
    False
    """""
    def label_counts(t):
        if is_leaf(t):
            return label(t)
        else:
            counts = {}
            for b in branches(t):
                for label, count in counts.items():
                    if label(t) not in counts.keys():
                        counts[label(t)] = 0
                    counts[label(t)] += label_counts(b)
                return counts
        return label_counts(t1) == label_counts(t2)

def decrypt(s, d):
    """List all possible decoded strings of s.
    >>> codes = {
    ... 'alan': 'spooky',
    ... 'al': 'drink',
    ... 'antu': 'your',
    ... 'turing': 'ghosts',
    ... 'tur': 'scary',
    ... 'ing': 'skeletons',
    ... 'ring': 'ovaltine'
    ... }
    >>> decrypt('alanturing', codes)
    ['drink your ovaltine', 'spooky ghosts', 'spooky scary skeletons']
    """
    if s == '':
        return []
    ms = []

    if s in d:
        ms.append(d[s])
    for k in range(1,len(s)+1):
        first, suffix = s[:k], s[k:]
        if first in d:
            for rest in decrypt(suffix, d):
                ms.append(d[first] + ' ' + rest)
    return ms



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

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def ensure_consistency(fn):
    """Returns a function that calls fn on its argument, returns fn's
        return value, and returns None if fn's return value is different
        from any of its previous return values for those same argument.
        Also returns None if more than 20 calls are made.
    >>> def consistent(x):
    ...     return x
    >>>
    >>> lst = [1, 2, 3]
    >>> def inconsistent(x):
    ...     return x + lst.pop()
    >>>
    >>> a = ensure_consistency(consistent)
    >>> a(5)
    5
    >>> a(5)
    5
    >>> a(6)
    6
    >>> a(6)
    6
    >>> b = ensure_consistency(inconsistent)
    >>> b(5)
    8
    >>> b(5)
    >>> b(6)
    7
    """
    n = 0
    z = {}
    def helper(x):
        nonlocal n
        n += 1
        if n > 20:
            return None
        val = fn(x)
        if x not in z:
            z[x] = [val]
        if [val] == z[x]:
            return val
        else:
            z[x] = None
            return None
    return helper
