class Value:
    def __init__(self, data, op='', parents=(),  label=''):
        self.data = data
        self.op = op
        self.parents = parents
        self.label = label

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'Værdien af data er {self.data}'

    def __add__(self, other):
        return Value(self.data + other.data, '+', (self, other))


class Deck:
    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'Kortspillet indeholder kortene {self.cards}'

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del self.cards[key]

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        d = Deck()
        d.cards = self.cards + other.cards
        return d