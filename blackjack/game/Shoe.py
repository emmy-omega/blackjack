import random

from blackjack.game.card import Card


class Shoe:
    """
    Class representing the decks' cards in the game

    Attributes
    ----------
    cards: list of cards to dealt during the game rounds
    """
    def __init__(self, decks=1):
        """
        Instantiate the Shoe, it's cards basing on deck numbers
        :param decks: Number of decks that make up the shoe
        """
        self.cards = []
        for i in range(decks):
            self.cards.extend([Card(rank=r, suit=s) for s in Card.suits for r in Card.ranks])

    def shuffle(self):
        """
        Randomize the card placings in the shoes
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Deal cards
        :return: card: A popped card from the shoe
        """
        return self.cards.pop()

