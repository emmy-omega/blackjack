import os
import time

from blackjack.common.constants import console


def display_cards(hands):
    os.system('clear')
    for hand in hands:
        # print(f'{hand.owner.role} <='.rjust(7, '-'))
        cards = hand.cards
        for card in cards:
            print('╭─', u'\U00002500', u'\U00002500', end='', sep='')
            if cards.index(card) == len(cards) - 1:
                print(u'\U00002500', u'\U00002500',
                      u'\U0000256E', end='', sep='')
        console.print(f'{hand.owner.role}', style="bold green")
        for card in cards:
            print(
                '│', card.rank if card.is_face_up else u'\U00002591', '', end='', sep=' ')
            if cards.index(card) == len(cards) - 1:
                print('', '', '│', end='', sep=' ')
        print(
            f"Total : {hand.total if len(cards) > 0 and cards[len(cards)-1].is_face_up else 'Unknown'}")
        for card in cards:
            print(
                '│', card.suit if card.is_face_up else u'\U00002591', '', end='', sep=' ')
            if cards.index(card) == len(cards) - 1:
                print('', '', '│', end='', sep=' ')
        print()
        print()
    time.sleep(2)
