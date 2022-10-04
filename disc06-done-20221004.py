def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest == Link.empty:
        return lnk.first
    else:
        return lnk.first + sum_nums(lnk.rest)

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    def mul(ls):
        total = 1
        for i in ls:
            total *= i
        return total

    rest_of_lnks = [lnk.rest for lnk in lst_of_lnks]
    first_of_lnks = [lnk.first for lnk in lst_of_lnks]
    curr_first = mul(first_of_lnks)
    if Link.empty in rest_of_lnks:
        return Link(curr_first)
    else:
        rest_mul_lnk = multiply_lnks(rest_of_lnks)
        return Link(curr_first,rest_mul_lnk)

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> unique
    Link(1, Link(5))
    >>> lnk
    Link(1, Link(5))
    """
    element = []
    def remove(lnk):
        if lnk.rest == Link.empty:
            return lnk
        else:
            if lnk.first not in element:
                element.append(lnk.first)
                rest_unique = remove(lnk.rest)
                lnk.rest = rest_unique
                return lnk
            else:
                return remove(lnk.rest)
    return remove(lnk)


def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i*lst[i] for i in range(len(lst)) if i%2==0]

def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if not lst:
        return []
    pivot = lst[0]
    less = [i for i in lst if i<pivot]
    greater = [j for j in lst if j>pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)

from functools import reduce

def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(lst) == 0:
        return 1
    result = 0
    splited = [lst[i::j] for i in range(len(lst)) for j in rnage(2, len(lst))]
    for ele in splited:
        tmp = reduce(mul, ele)
        if result < temp:
            result = temp
    return temp

def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> print_levels(redundant_map(tree, double))
    [2] # 1 * 2 ? (1) ; Apply double one time
    [4, 8] # 1 * 2 ? (2), 2 * 2 ? (2) ; Apply double two times
    [16] # 1 * 2 ? (2 ? 2) ; Apply double four times
    [256] # 1 * 2 ? (2 ? 3) ; Apply double eight times
    """


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    def insert_tail(self, link):
        assert link is Link.empty or isinstance(link, Link)
        if self.rest == Link.empty:
            self.rest = link
        else:
            self.rest.insert_tail(link)

# Tree Class
class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])
