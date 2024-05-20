import csv
import random
from cards import Carta
from collections import Counter

def main():
    my_nick = input('\nNickname: ')
    print()
    # n°1
    player_list = players()
    print()
    # n°2
    deck = set_deck()
    # n°3
    players_cards, deck = pocket_cards(player_list, deck)
    # n°4
    deck, community_cards = flop(deck)
    print(f"Your hand: {' '.join([str(c) for c in players_cards[0]])}")
    print(f"Board: {' '.join([str(c) for c in community_cards])}", '\n')
    while True:
        next_play = input('Do you CHECK or RAISE? ')
        if next_play.strip().lower() in ['check', 'raise']:
            break
        else:
            print('Invalid input.')
    print()
    if next_play.strip().lower() == 'check':
        # n°5
        player_data = show_cards(players_cards, community_cards)
        for i in range(len(player_data)):
            if i == 0:
                print(f"{my_nick} has a {player_data[i]['hand']}!")
                print(' '.join([str(c) for c in player_data[i]['5cards']]), '\n')
            else:
                print(f"CPU{i} has a {player_data[i]['hand']}!")
                print(' '.join([str(c) for c in player_data[i]['5cards']]), '\n')
        # n°7
        winner = winner_hand(player_data)
        if winner == 0:
            print(f'The winner is {my_nick}')
        elif isinstance(winner, int):
            print(f'The winner is CPU{winner}')
        elif winner == None:
            print(f"There's no winner, it's a tie!")
    elif next_play.strip().lower() == 'raise':
        # n°4
        deck, community_cards = turn(deck, community_cards)
        print(f"Your hand: {' '.join([str(c) for c in players_cards[0]])}")
        print(f"Board: {' '.join([str(c) for c in community_cards])}", '\n')
        while True:
            next_play = input('Do you CHECK or RAISE? ')
            if next_play.strip().lower() in ['check', 'raise']:
                break
            else:
                print('Invalid input.')
        print()
        if next_play.strip().lower() == 'check':
            # n°5
            player_data = show_cards(players_cards, community_cards)
            for i in range(len(player_data)):
                if i == 0:
                    print(f"{my_nick} has a {player_data[i]['hand']}!")
                    print(f"Hand: {' '.join([str(c) for c in player_data[i]['5cards']])} | Extras: {' '.join([str(c) for c in player_data[i]['remains']])}\n")
                else:
                    print(f"CPU{i} has a {player_data[i]['hand']}!")
                    print(f"Hand: {' '.join([str(c) for c in player_data[i]['5cards']])} | Extras: {' '.join([str(c) for c in player_data[i]['remains']])}\n")
            # n°7
            winner = winner_hand(player_data)
            if winner == 0:
                print(f'The winner is {my_nick}')
            elif isinstance(winner, int):
                print(f'The winner is CPU{winner}')
            elif winner == None:
                print(f"There's no winner, it's a tie!")
        elif next_play.strip().lower() == 'raise':
            # n°4
            deck, community_cards = river(deck, community_cards)
            print(f"Your hand: {' '.join([str(c) for c in players_cards[0]])}")
            print(f"Board: {' '.join([str(c) for c in community_cards])}", '\n')
            input('Press enter to SHOWDOWN!!! ')
            print()
            # n°5
            player_data = show_cards(players_cards, community_cards)
            for i in range(len(player_data)):
                if i == 0:
                    print(f"{my_nick} has a {player_data[i]['hand']}!")
                    print(f"Hand: {' '.join([str(c) for c in player_data[i]['5cards']])} | Extras: {' '.join([str(c) for c in player_data[i]['remains']])}\n")
                else:
                    print(f"CPU{i} has a {player_data[i]['hand']}!")
                    print(f"Hand: {' '.join([str(c) for c in player_data[i]['5cards']])} | Extras: {' '.join([str(c) for c in player_data[i]['remains']])}\n")
            # n°7
            winner = winner_hand(player_data)
            if winner == 0:
                print(f'The winner is {my_nick}')
            elif isinstance(winner, int):
                print(f'The winner is CPU{winner}')
            elif winner == None:
                print(f"There's no winner, it's a tie!")

# n°1
def players() -> list[list]:
    players = []
    while True:
        try:
            n = input('Number of players: ')
            n = int(n)
            if 2 <= n <= 10:
                for p in range(n):
                    players.append(list())
                return players
            else:
                print('Out of range! Max n° of players is 10.')
        except ValueError:
            print('Invalid input of players.')

# n°2
def set_deck() -> list:
    deck = []
    with open('cards.csv') as file:
        reader = csv.DictReader(file)
        for line in reader:
            deck.append(Carta(line['simbolo'], line['palo']))
    random.shuffle(deck)
    return deck

# n°3
def pocket_cards(l: list[list], d: list) -> {list[list], list}:
    for _ in range(2):
        for p in range(len(l)):
            given_Card = d.pop()
            l[p].append(given_Card)
    return l, d
     
# n°4
def flop(d: list):
    board = []
    flop = [d.pop() for _ in range(3)]
    board.extend(flop)
    return d, board
def turn(d: list, b: list):
    board = b
    board.append(d.pop())
    return d, board
def river(d: list, b: list):
    board = b
    board.append(d.pop())
    return d, board

# n°5
def show_cards(play_c: list[list], comm_c: list) -> list[dict]:
    player_data = []
    for p in range(len(play_c)):
        hand = play_c[p] + comm_c
        # n°6
        used, not_used, hand_name = best_hand(hand)
        player_data.append({'5cards': used, 'remains': not_used, 'hand': hand_name})
    return player_data

# n°6
def best_hand(hand: list[Carta]):
    # For executate break I was using the condition 'if used and not_used:' wich does not allow not_used
    # to be blank, so it just enough with 'if used:'.
    used = []
    not_used = []
    hands_func = [royal_flush, straight_flush, quads, full_house, flush, straight, trips, two_pair, pair, high_card]

    for f in hands_func:
        used, not_used = f(hand)
        hand_name = f.__name__
        if used:
            break

    hand_name = hand_name.replace('_', ' ').title()

    return used, not_used, hand_name

def royal_flush(hand: list[Carta]):
    ## The first attempt was very primitive, without iterations for multiple cases, let alone methods,
    # actually I used the value method for sorting, but that was it for the raw schema.
    ## Anyway, due to the inability of using in for object comparison, I had to use the special method 
    # __eq__ (thank god I found this concept, it took a lot to time to understand the issue :'D).
    ## For the hand ['Kh', 'Qs', '9h', '9s', '5c', '4s', '2d'] it was the problem that if there was no
    # 'A', it was forced to be royal_flush bc of the lack of else statement to negate it.
    used = []
    not_used = []
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    for i in range(3):
        if sorted_hand[i].simbolo == 'A':
            for c in range(5):
                if sorted_hand[i].xcard(c) not in hand:
                    is_rflush = False
                    break
                start_c = Carta('A', sorted_hand[i].palo)
                is_rflush = True
            if is_rflush:
                break
        else:
            is_rflush = False

    if is_rflush:
        for c in sorted_hand:
            if c in [start_c.xcard(_) for _ in range(5)]:
                used.append(c)
            else:
                not_used.append(c)
    
    return used, not_used

def straight_flush(hand: list[Carta]):
    # During the crafting of straight a bug was found, in the block with break. It was necessary to add
    # flag = True, to cover the case in which the 2 highest cards are consecutive and from the same suit,
    # bc it'd set the flag as False and it'd stop the loop without checking the third highest. The same
    # applies to royal_flush, already covered.
    used = []
    not_used = []
    flag = True
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    for _ in range(3):
        if flag:
            for c in range(5):
                if sorted_hand[_].xcard(c) not in hand:
                    is_sflush = False
                    flag = True
                    break
                start_c = Carta(sorted_hand[_].simbolo, sorted_hand[_].palo)
                is_sflush = True
                flag = False

    if is_sflush:
        for c in sorted_hand:
            if c in [start_c.xcard(_) for _ in range(5)]:
                used.append(c)
            else:
                not_used.append(c)

    return used, not_used

def quads(hand: list[Carta]):
    # Most of the poker hand functions from now will use remove, pop and hand n sorted_hand at the same
    # time bc one cannot iterate and remove elementos from the same list at once.
    used = []
    not_used = []
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    counter = Counter([c.simbolo for c in hand])
    if counter.most_common(1)[0][1] == 4:
        all_suit = Carta(counter.most_common(1)[0][0], 'spade')
        is_quads = True
    else:
        is_quads = False

    if is_quads:
        for c in hand:
            if c in all_suit.xcard(0, 'all'):
                sorted_hand.remove(c)
                used.append(c)
        used.append(sorted_hand.pop(0))
        not_used.extend(sorted_hand)

    return used, not_used

def full_house(hand: list[Carta]):
    ## For this function, it was very important to know that Counter cares about the order of elements.
    ## Spade artifice: It means that in order to use xcard(0, 'all'), it's necessary to have a Carta object,
    # so I deliberately assign as suit for our card w/ duplicates the 'spade', just to get all 4 suits.
    used = []
    not_used = []
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    counter = Counter([c.simbolo for c in sorted_hand])
    if counter.most_common(2)[0][1] == 3 and counter.most_common(2)[1][1] in [3, 2]:
        all_suit1 = Carta(counter.most_common(2)[0][0], 'spade')
        all_suit2 = Carta(counter.most_common(2)[1][0], 'spade')
        is_fhouse = True
    else:
        is_fhouse = False

    if is_fhouse:
        for c in hand:
            if c in all_suit1.xcard(0, 'all'):
                sorted_hand.remove(c)
                used.append(c)
        for c in hand:
            if c in all_suit2.xcard(0, 'all') and len(used) < 5:
                sorted_hand.remove(c)
                used.append(c)
        not_used.extend(sorted_hand)     
    
    return used, not_used

def flush(hand: list[Carta]):
    used = []
    not_used = []
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    counter = Counter([c.palo for c in hand])
    if counter.most_common(1)[0][1] >= 5:
        com_p = counter.most_common(1)[0][0]
        is_flush = True
    else:
        is_flush = False

    if is_flush:
        for c in sorted_hand:
            if c.palo == com_p and len(used) < 5:
                used.append(c)
            else:
                not_used.append(c)

    return used, not_used

def straight(hand: list[Carta]):
    ## While crafting straight this redundant code line was found: for c in [x for x in range(5)], it was
    # repeated in royal_flush, straight_flush and this one. Solved simply by getting rid of the comprehension.
    ## During the crafting of straight, xcard v2.0 was created/implemented. It was in order to get the lists of
    # all suits for the x previous card. This also helped to get the lines of code from quads and full_house 
    # more concise, because it was full of raw lists with all the cases for each suit.
    ## This function was very tricky, but any along with xcard v2.0 could handle it B).
    used = []
    not_used = []
    flag = True
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    for i in range(3):
        if flag:
            for l in [sorted_hand[i].xcard(_, 'all') for _ in range(5)]:
                if any(c in hand for c in l):
                    start_c = Carta(sorted_hand[i].simbolo, sorted_hand[i].palo)
                    is_straight = True
                    flag = False
                else:
                    is_straight = False
                    flag = True
                    break
    
    if is_straight:
        for l in [start_c.xcard(_, 'all') for _ in range(5)]:
            for c in hand:
                if c in l and len(used) < 5:
                    sorted_hand.remove(c)
                    used.append(c)
                    break
        not_used.extend(sorted_hand)

    return used, not_used

def trips(hand: list[Carta]):
    # Spade artifice.
    used = []
    not_used = []
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    counter = Counter(c.simbolo for c in hand)
    if counter.most_common(2)[0][1] == 3 and counter.most_common(2)[1][1] == 1:
        all_suit = Carta(counter.most_common(2)[0][0], 'spade')
        is_trips = True
    else:
        is_trips = False

    if is_trips:
        for c in hand:
            if c in all_suit.xcard(0, 'all'):
                sorted_hand.remove(c)
                used.append(c)
        for _ in range(2):
            used.append(sorted_hand.pop(0))
        not_used.extend(sorted_hand)
    
    return used, not_used

def two_pair(hand: list[Carta]):
    # Spade artifice.
    used = []
    not_used = []
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    counter = Counter(c.simbolo for c in sorted_hand)
    if counter.most_common(2)[0][1] == 2 and counter.most_common(2)[1][1] == 2:
        all_suit1 = Carta(counter.most_common(2)[0][0], 'spade')
        all_suit2 = Carta(counter.most_common(2)[1][0], 'spade')
        is_twopair = True
    else:
        is_twopair = False

    if is_twopair:
        for c in hand:
            if c in all_suit1.xcard(0, 'all'):
                sorted_hand.remove(c)
                used.append(c)
        for c in hand:
            if c in all_suit2.xcard(0, 'all'):
                sorted_hand.remove(c)
                used.append(c)
        used.append(sorted_hand.pop(0))
        not_used.extend(sorted_hand)
    
    return used, not_used

def pair(hand: list[Carta]):
    # Spade artifice.
    used = []
    not_used = []
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    counter = Counter(c.simbolo for c in sorted_hand)
    if counter.most_common(2)[0][1] == 2 and counter.most_common(2)[1][1] == 1:
        all_suit = Carta(counter.most_common(2)[0][0], 'spade')
        is_pair = True
    else:
        is_pair = False

    if is_pair:
        for c in hand:
            if c in all_suit.xcard(0, 'all'):
                sorted_hand.remove(c)
                used.append(c)
        for _ in range(3):
            used.append(sorted_hand.pop(0))
        not_used.extend(sorted_hand)
    
    return used, not_used

def high_card(hand: list[Carta]):
    # This last poker hand function it's made in such a way that all the symbols must be different. It's not
    # as if just any hand can pass through and get as a result that it's indeed a high_card.
    used = []
    not_used = []
    sorted_hand = sorted(hand, key=Carta.value, reverse=True)

    counter = Counter(c.simbolo for c in hand)
    if counter.most_common(1)[0][1] == 1:
        is_highcard = True
    else:
        is_highcard = False

    if is_highcard:
        for c in range(len(hand)):
            if c < 5:
                used.append(sorted_hand[c])
            else:
                not_used.append(sorted_hand[c])
    
    return used, not_used

# n°7
def winner_hand(play_d: list[dict]):
    h_rank = {'Royal flush': 10, 'Straight Flush': 9, 'Quads': 8, 'Full House': 7, 'Flush': 6, 'Straight': 5, 'Trips': 4, 'Two Pair': 3, 'Pair': 2, 'High Card': 1}
    stronger = []
    # n°5
    for i, p in enumerate(play_d):
        stronger.append([i, p['hand'], p['5cards']])
    sorted_stronger = sorted(stronger, key=lambda x: (h_rank[x[1]], x[2][0].value(), x[2][1].value(), x[2][2].value(), x[2][3].value(), x[2][4].value()), reverse=True)
    tiebreaker = [x for x in sorted_stronger if x[1] == sorted_stronger[0][1]]
    for _ in range(len(tiebreaker)):
        for j in range(5):
            if tiebreaker[0][2][j].value() == tiebreaker[_][2][j].value() and len(tiebreaker) > 1:
                atie = True
            else:
                atie = False
                break
        if not atie:
            break
    if atie:
        return None
    else:
        return tiebreaker[0][0]

if __name__ == '__main__':
    main()
