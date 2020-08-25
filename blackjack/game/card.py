import random


class Card:
    """
    Class represent a card

    Attributes
    ----------
    rank: str
    suit: str
    is_face_up: bool
        Determines whether the cards face is hidden or not

    Methods
    -------
    type()
        Determines whether a card is low or high card
    generate()
        Constructs an instance of card of a random suit
    weight()
        Determines the weight of the card based on it rank
    value()
        Determines the weight of the card based on it rank
    """
    suits = ('♣', '♦', '♠', '♥')
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

    def __init__(self, rank, suit=random.choice(suits)):
        self.rank = rank
        self.suit = suit
        self.is_face_up = True

    @property
    def type(self):
        """
        Determines whether a card is low or high card based on the rank
        :return: type(str)
            the type of card; either "high" or "low"
        """
        if self.rank in Card.ranks[:8]:
            return "low"
        elif self.rank in Card.ranks[-5:]:
            return "high"

    @classmethod
    def generate(cls, rank):
        """
        Constructs an instance of card of a random suit
        :param rank: the card rank to generate
        :return: card(Card)
            New card of said rank but random suit
        """
        return cls(rank=rank)

    @property
    def weight(self):
        """
        Determines the weight of the card based on it rank; high cards except ace weight 10. the rest weigh their rank
        value

        :return: weight(int)
            Weight of the card
        """
        if self.rank in [str(r) for r in range(2, 10)]:
            return int(self.rank)
        elif self.rank == 'A':
            return 1
        else:
            return 10

    @property
    def value(self):
        """
        Determines the weight of the card based on it rank
        :return: value(int)
            either -1, 0 or 1
        """
        if self.rank in [str(r) for r in range(2, 7)]:
            return -1
        elif self.rank in [str(r) for r in range(7, 10)]:
            return 0
        else:
            return 1
