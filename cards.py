class Carta():

    palo_unicode = {'spade': '\u2660', 'heart': '\u2665', 'club': '\u2663', 'diamond': '\u2666'}
    value_dict = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

    def __init__(self, simbolo: str, palo: str):
        self.simbolo = simbolo
        self.palo = palo
        if self.palo in ['heart', 'diamond']:
            color = 'red'
        elif self.palo in ['spade', 'club']: 
            color = 'black'
        self.color = color

    def __str__(self):
        return f'{self.simbolo}{self.palo_unicode[self.palo]}'
    
    ## This special method was critical to be able to compare if the objects are or not in a list.
    ## Such a struggle not knowing this method from the start :S.
    def __eq__(self, other: object):
        if isinstance(other, Carta) and self.simbolo == other.simbolo and self.palo == other.palo:
            return True
    
    def value(self):
        for k, v in self.value_dict.items():
            if v == self.simbolo:
                return k

    ## The first idea was to determinate a method to get the next card, but due to the possibility of getting a hand with 7 cards 
    # same suit, it'd be better to use the higher value and go backwards.
    ## So ncard (next card) turn into xcard method. The right name should be pcard (previous card) though wcyd xD. 
    ## xcard v2.0 was created in order to get the list of 4 cards with the same suit from a card, just to reduce space ("efficiency").
    def xcard(self, x: int=0, p: str=None):
        if x == 0:
            xsim = self.simbolo
        elif x == 1:
            if self.value() == 2:
                xsim = 'A'
            else:
                xsim = self.value_dict[(self.value() - 1)]
        elif x == 2:
            if self.value() == 2:
                xsim = 'K'
            elif self.value() == 3:
                xsim = 'A'
            else:
                xsim = self.value_dict[(self.value() - 2)]
        elif x == 3:
            if self.value() == 2:
                xsim = 'Q'
            elif self.value() == 3:
                xsim = 'K'
            elif self.value() == 4:
                xsim = 'A'
            else:
                xsim = self.value_dict[(self.value() - 3)]
        elif x == 4:
            if self.value() == 2:
                xsim = 'J'
            elif self.value() == 3:
                xsim = 'Q'
            elif self.value() == 4:
                xsim = 'K'
            elif self.value() == 5:
                xsim = 'A'
            else:
                xsim = self.value_dict[(self.value() - 4)]
        else:
            raise ValueError('xcard method: Not a valid input.')
        if p == None:
            xpal = self.palo
            return Carta(xsim, xpal)
        elif p in ['spade', 'heart', 'club', 'diamond']:
            xpal = p
            return Carta(xsim, xpal)
        elif p == 'all':
            return [Carta(xsim, c) for c in ['spade', 'heart', 'club', 'diamond']]
        else:
            raise ValueError('xcard method: Not a valid input.')
        