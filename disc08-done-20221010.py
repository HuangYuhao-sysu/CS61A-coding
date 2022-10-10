def reverse(lst):
    def reverse_sofar(lst, lst_sofar):
        if lst == Link.empty:
            return lst_sofar
        else:
            return reverse_sofar(lst.rest, Link(lst.first, lst_sofar))
    return reverse_sofar(lst, Link.empty)

def append(lsta, lstb):
    rev_lsta = reverse(lsta)
    if rev_lsta == Link.empty:
        return lstb
    else:
        return append(reverse(rev_lsta.rest), Link(rev_lsta.first, lstb))          

# Link class
class Link:
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

lsta = Link(5, Link(4, Link(3)))
lstb = Link(2, Link(1, Link(0)))
print(append(lsta, lstb))