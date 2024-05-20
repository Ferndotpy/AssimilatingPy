from cards import Carta
from project import *

def test_royal_flush():
    hand = [Carta('K', 'spade'), Carta('A', 'spade'), Carta('A', 'heart'), Carta('10', 'heart'), Carta('J', 'heart'), Carta('Q', 'heart'), Carta('K', 'heart')]
    u, n = royal_flush(hand)
    assert u == [Carta('A', 'heart'), Carta('K', 'heart'), Carta('Q', 'heart'), Carta('J', 'heart'), Carta('10', 'heart')] 
    assert n == [Carta('A', 'spade'), Carta('K', 'spade')]

def test_straight_flush():
    hand = [Carta('10', 'club'), Carta('9', 'club'), Carta('8', 'club'), Carta('7', 'club'), Carta('6', 'club'), Carta('J', 'spade'), Carta('Q', 'club')]
    u, n = straight_flush(hand)
    assert u == [Carta('10', 'club'), Carta('9', 'club'), Carta('8', 'club'), Carta('7', 'club'), Carta('6', 'club')]
    assert n == [Carta('Q', 'club'), Carta('J', 'spade')]

def test_quads():
    hand = [Carta('2', 'club'), Carta('Q', 'heart'), Carta('Q', 'diamond'), Carta('Q', 'club'), Carta('Q', 'spade'), Carta('5', 'heart'), Carta('5', 'spade')]
    u, n = quads(hand)
    assert u == [Carta('Q', 'heart'), Carta('Q', 'diamond'), Carta('Q', 'club'), Carta('Q', 'spade'), Carta('5', 'heart')]
    assert n == [Carta('5', 'spade'), Carta('2', 'club')]

def test_full_house():
    hand = hand = [Carta('Q', 'heart'), Carta('Q', 'spade'), Carta('7', 'diamond'), Carta('7', 'club'), Carta('Q', 'diamond'), Carta('10', 'club'), Carta('10', 'heart')]
    u, n = full_house(hand)
    assert u == [Carta('Q', 'heart'), Carta('Q', 'spade'), Carta('Q', 'diamond'), Carta('10', 'club'), Carta('10', 'heart')]
    assert n == [Carta('7', 'diamond'), Carta('7', 'club')]

def test_flush():
    hand = [Carta('K', 'club'), Carta('2', 'club'), Carta('6', 'heart'), Carta('7', 'club'), Carta('10', 'club'), Carta('A', 'spade'), Carta('5', 'club')]
    u, n = flush(hand)
    assert u == [Carta('K', 'club'), Carta('10', 'club'), Carta('7', 'club'), Carta('5', 'club'), Carta('2', 'club')]
    assert n == [Carta('A', 'spade'), Carta('6', 'heart')]

def test_straight():
    hand = [Carta('3', 'heart'), Carta('7', 'diamond'), Carta('6', 'club'), Carta('5', 'spade'), Carta('4', 'heart'), Carta('J', 'heart'), Carta('3', 'club')]
    u, n = straight(hand)
    assert u == [Carta('7', 'diamond'), Carta('6', 'club'), Carta('5', 'spade'), Carta('4', 'heart'), Carta('3', 'heart')]
    assert n == [Carta('J', 'heart'), Carta('3', 'club')]

def test_trips():
    hand = hand = [Carta('K', 'diamond'), Carta('J', 'heart'), Carta('J', 'diamond'), Carta('J', 'club'), Carta('7', 'club'), Carta('3', 'heart'), Carta('A', 'spade')]
    u, n = trips(hand)
    assert u == [Carta('J', 'heart'), Carta('J', 'diamond'), Carta('J', 'club'), Carta('A', 'spade'), Carta('K', 'diamond')]
    assert n == [Carta('7', 'club'), Carta('3', 'heart')]

def test_two_pair():
    hand = [Carta('8', 'club'), Carta('Q', 'heart'), Carta('6', 'club'), Carta('10', 'club'), Carta('10', 'spade'), Carta('8', 'heart'), Carta('6', 'spade')]
    u, n = two_pair(hand)
    assert u == [Carta('10', 'club'), Carta('10', 'spade'), Carta('8', 'club'), Carta('8', 'heart'), Carta('Q', 'heart')]
    assert n == [Carta('6', 'club'), Carta('6', 'spade')]

def test_pair():
    hand = [Carta('9', 'heart'), Carta('9', 'spade'), Carta('5', 'club'), Carta('4', 'spade'), Carta('2', 'diamond'), Carta('J', 'diamond')]
    u, n = pair(hand)
    assert u == [Carta('9', 'heart'), Carta('9', 'spade'), Carta('J', 'diamond'), Carta('5', 'club'), Carta('4', 'spade')]
    assert n == [Carta('2', 'diamond')]

def test_high_card():
    hand = [Carta('K', 'heart'), Carta('10', 'diamond'), Carta('7', 'club'), Carta('6', 'club'), Carta('5', 'club'), Carta('A', 'spade')]
    u, n = high_card(hand)
    assert u == [Carta('A', 'spade'), Carta('K', 'heart'), Carta('10', 'diamond'), Carta('7', 'club'), Carta('6', 'club')]
    assert n == [Carta('5', 'club')]

def test_best_hand():
    hand = [Carta('Q', 'heart'), Carta('Q', 'spade'), Carta('10', 'diamond'), Carta('10', 'club'), Carta('Q', 'diamond'), Carta('10', 'spade'), Carta('A', 'heart')]
    u, n, h = best_hand(hand)
    assert u == [Carta('Q', 'heart'), Carta('Q', 'spade'), Carta('Q', 'diamond'), Carta('10', 'diamond'), Carta('10', 'club')]
    assert n == [Carta('A', 'heart'), Carta('10', 'spade')]
    assert h == 'Full House'
