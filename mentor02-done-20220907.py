

def is_prime(x):
    if x==1:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True


def all_primes(nums):
    """
    Return all primes in nums.

    >>> nums = [1,3,6,9,11,13,15,20,23]
    >>> all_primes(nums)
    [1, 3, 11, 13, 23]
    """
    return [x for x in nums if is_prime(x)]

def list_of_lists(lst):
    """

    >>> list_of_lists([1,2,3])
    [[0], [0, 1], [0, 1, 2]]
    >>> list_of_lists([1])
    [[0]]
    >>> list_of_lists([])
    []
    """
    return [[0] if i==0 else [0]+lst[:i] for i in range(len(lst))]

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

def sum_of_nodes(t):
    """

    >>> a=tree(9,[tree(2),tree(4,[tree(1)]),tree(4,[tree(7),tree(3)])])
    >>> sum_of_nodes(a)
    30
    """
    if is_leaf(t):
        return label(t)
    else:
        sum_of_branches = [sum_of_nodes(b) for b in branches(t)]
        return sum(sum_of_branches)+label(t)
