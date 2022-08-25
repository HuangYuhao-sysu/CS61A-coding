# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    else:
        for branch in branches(tree):
            if not is_tree(branch):
                return False
    return True

# For convenience
def is_leaf(tree):
    return not branches(tree)

t = tree(1,
         [tree(3,
               [tree(4),
                tree(5),
                tree(6)]),
          tree(2)])


def tree_max(t):
    if is_leaf(t):
        return label(t)
    else:
        branch_max = [tree_max(b) for b in branches(t)]
        return max(branch_max)

def height(t):
    if is_leaf(t):
        return 0
    else:
        branch_height = [1+height(b) for b in branches(t)]
        return max(branch_height)


def square_tree(t):
    return tree(label(t)*label(t), [square_tree(b) for b in branches(t)])

def has_value(t, x):
    """


    """
    if not branches(t) and label(t) != x:
        return False
    elif label(t) == x:
        return True
    else:
        branch_has = [has_value(b, x) for b in branches(t)]
        return True in branch_has

def find_path(t, x):
    """

    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    """
    if label(t) == x:
        return [x]
    elif is_leaf(t) and label(t) != x:
        return False
    else:
        branch_path = []
        branch_find = [b for b in branches(t) if has_value(b, x)]
        for b in branch_find:
            branch_path = find_path(b, x)
        if branch_path == []:
            return None
        else:
            return [label(t)]+branch_path

def leaves(t):
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(t)], [])


def get_leaf_height(t):
    """Return a list with list containing all leaf and its height"""
    t_leaves = leaves(t)
    leaves_height = []
    for leaf in t_leaves:
        leaf_path = []
        leaf_path = find_path(t, leaf)
        leaf_height = len(leaf_path)-1
        leaves_height += [[leaf, leaf_height]]
    return leaves_height

def remove_leaf(t, x):
    """Return a tree remove leaf of value x"""
    if has_value(t, x) and height(t) == 1:
        new_b = [b for b in branches(t) if not has_value(b, x)]
        return tree(label(t), new_b)
    else:
        new_re_b = [remove_leaf(b, x) for b in branches(t)]
        return tree(label(t), new_re_b)

def prune(t, k):
    leaves_height = get_leaf_height(t)
    for leaf, height in leaves_height:
        if height > k:
            t = remove_leaf(t, leaf)
    return t
