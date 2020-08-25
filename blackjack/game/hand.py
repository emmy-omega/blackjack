class Hand:
    """
    Class to representing hand participating in the game rounds

    Attributes
    ---------
    owner: Player
        The player to which the hand belongs
    cards: Card
        List of cards in the hand
    state: str
        Game state of the hand
    is_splittable: bool
        Determines whether the hand can be split

    Methods
    -------
    split()
        Splits the hand into two
    totals()
        Calculates the hard and soft total of the hand
    totals()
        Calculate the optimum total of the hand
    is_soft()
        Determines whether a hand contains a ace card
    is_paired()
        Determines whether a hands two cards are of the same rank
    is_blackjack
        Determines if hand contains an aces and another high card
    """
    def __init__(self, owner):
        self.owner = owner
        self.cards = []
        self.state = 'in'
        self.is_splittable = True
        self.bet = 0

    def split(self):
        """
        Split the hand into two, sharing the cards; with each taking one
        :return: hand(Hand): The newly creating hand
        """
        return Hand(owner=self.owner)

    @property
    def totals(self):
        """
        Calculate the hard and soft total of the hand
        :return: total
            tuple of the hard and soft totals
        """
        non_ace_weights = [c.weight for c in self.cards if not c.rank == "A"]
        total = sum(non_ace_weights)
        if self.is_soft:
            soft_total = 0
            num_aces = len([c for c in self.cards if c.rank == "A"])
            if num_aces > 1:
                soft_total += (num_aces - 1) + 11
                return total + num_aces, total + (num_aces - 1) + 11
            else:
                return total + 1, total + 11
        else:
            return total, 0

    @property
    def total(self):
        """
        Chooses the best placed total from totals to win a round
        :return: total(int)
            Optimum total
        """
        return max(self.totals) if max(self.totals) < 22 or min(self.totals) == 0 else min(self.totals)

    @property
    def is_blackjack(self):
        """
        Determines if hand contains an aces and another high card
        :return: truthy(bool)
        """
        high_cards = [c for c in self.cards if c.type == "high"]
        aces = [c for c in self.cards if c.rank == "A"]
        if len(self.cards) == 2 and len(high_cards) == 2 and self.is_soft and len(aces) == 1:
            return True
        return False

    @property
    def is_soft(self):
        """
        Determines whether a hand contains a ace card
        :return: truthy(bool)
        """
        aces = [c for c in self.cards if c.rank == "A"]
        if len(aces) > 0:
            return True
        return False

    @property
    def is_paired(self):
        """
        Determines whether a hands two cards are of the same rank
        :return: truthy(bool)
        """
        if len(self.cards) == 2 and self.cards[0].rank == self.cards[1].rank:
            return True
        return False

