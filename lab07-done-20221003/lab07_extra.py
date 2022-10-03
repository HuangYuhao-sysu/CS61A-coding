""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    if link.rest != Link.empty:
        if link.rest.first == value:
            link.rest = link.rest.rest
            remove_all(link, value)
        else:
            remove_all(link.rest, value)


# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if isinstance(link.first, int):
        link.first = fn(link.first)
    else:
        deep_map_mut(fn, link.first)

    if link.rest == Link.empty:
        return None
    else:
        deep_map_mut(fn, link.rest)

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    has_found = []
    def find(link):
        if link.rest == Link.empty:
            return False
        elif link.rest in has_found:
            return True
        else:
            has_found.append(link.rest)
            return find(link.rest)
    return find(link)

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    has_found = []
    def find(link):
        if link.rest == Link.empty:
            return False
        elif link.rest in has_found:
            return True
        else:
            has_found.append(link.rest)
            return find(link.rest)
    return find(link)

# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return None
    else:
        even_labels = [b.label for b in t.branches if b.label%2==0]
        if even_labels:
            all_labels = [b.label for b in t.branches]
            l = len(all_labels)
            if l%2 == 0:
                for i in range(int(l/2)):
                    t.branches[i].label, t.branches[l-1-i].label = t.branches[l-1-i].label, t.branches[i].label
            else:
                for i in range(int((l-1)/2)):
                    t.branches[i].label, t.branches[l-1-i].label = t.branches[l-1-i].label, t.branches[i].label
        for b in t.branches:
            reverse_other(b)




