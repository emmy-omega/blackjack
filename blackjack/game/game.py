from blackjack.game.hand import Hand
from blackjack.common.constants import state, role
from blackjack.common.helper import display_cards
from blackjack.game.player import Player


def verifyDealer(players):
    """
    Verify the presence of the dealer and player

    :param players: Players to participate in the game's round/s
    :return: players: Tuple of the dealer and player
    """
    if len(players) > 2 or len(players) < 2:
        raise ValueError("game current accepts exactly two player")
    dealers = [p for p in players if p.role == 'Dealer']
    if len(dealers) > 1 or len(dealers) < 1:
        raise ValueError("game must have exactly only dealer!")
    return next(p for p in players if p.role == 'Dealer'), next(p for p in players if p.role == 'Player')


def getPlayerHands(hands):
    """
    Filter hand of the "Player role"

    :param hands: All hands participating in the round
    :return: list of player hands
    """
    return [hand for hand in hands if hand.owner.role == role.PLAYER]


def getPlayerHand(hands):
    """
    Find the player hand

    :param hands: All hand participating in the round
    """
    return next(
            (hand for hand in hands if hand.owner.role == role.PLAYER), None)


def getDealerHand(hands):
    """
    Find the dealer hand

    :param hands: All hand participating in the round
    """
    return next(
            (hand for hand in hands if hand.owner.role == role.DEALER), None)


class Game:
    """
    Represent a game of blackjack
    ...
    Attributes
    ----------
    dealer: Player
        Represents the house dealer
    player: Player
        Represents the game player

    Methods
    -------
    start_round()
        Executes a round of blackjack

    deal_init_cards(hands)
        Deals each player their two cards

    play_player_hand(hand, hands, player_hands)
        Executes a player actions sequence

    play_dealer_hand(hands)
        Executes dealer actions sequence

    get_winners(hands)
        Determines the winner hand/s
    """

    def __init__(self, players, shoe):
        self.dealer, self.player = verifyDealer(players)
        self.shoe = shoe

    @property
    def start_round(self):
        """
        Execute a round of blackjack game.

            :returns
            hands(list): List of Hand that took part

        """
        self.shoe.shuffle()
        hands = [Hand(self.dealer), Hand(self.player)]
        player_hand = getPlayerHand(hands)
        dealer_hand = getDealerHand(hands)

        self.deal_init_cards(hands)

        # check if dealer has blackjack
        if dealer_hand.is_blackjack:
            dealer_hand.cards[1].is_face_up = True
            display_cards(hands)
            # end round
            return hands
        # check if player has is blackjack
        elif player_hand.is_blackjack:
            dealer_hand.cards[1].is_face_up = True
            display_cards(hands)
            # end round
            return hands

        if not player_hand.is_blackjack:
            player_hands = getPlayerHands(hands)
            while len(player_hands) != 0:
                hand = player_hands.pop()
                if not hand.is_blackjack:
                    self.play_player_hand(hand, hands, player_hands)
                else:
                    break
        # check if all player hands are bust
        bust_player_hands = [hand for hand in hands if hand.owner.role == role.PLAYER and hand.state == state.BUST]
        if not len(bust_player_hands) == len(getPlayerHands(hands)):
            self.play_dealer_hand(hands)
        return hands

    def deal_init_cards(self, hands):
        """
        Deals the dealer and player their two initial cards.

        Starting with the player and alternating till each has two cards from which the game, dealer and player can
        start making decisions

        :param hands: hands instantiated for the round
        """
        player_hand = getPlayerHand(hands)
        dealer_hand = getDealerHand(hands)

        player_hand.cards.append(self.shoe.deal())
        display_cards(hands)
        dealer_hand.cards.append(self.shoe.deal())
        display_cards(hands)
        player_hand.cards.append(self.shoe.deal())
        display_cards(hands)
        dealer_2nd_card = self.shoe.deal()
        dealer_2nd_card.is_face_up = False
        dealer_hand.cards.append(dealer_2nd_card)
        display_cards(hands)

    def play_player_hand(self, hand, hands, player_hands):
        """
        Executes a player hand sequence of action.

        The updates the state of the player's hand in reaction to player decisions and changes to cards in the hand

        :param hand: the players hand(one of) being acted upon
        :param hands: All hands participating in the round
        :param player_hands: All hands the belong to the player
        """
        while hand.state == state.IN:
            if not hand.is_splittable and len(hand.cards) == 1:
                hand.cards.append(self.shoe.deal())
                display_cards(hands)
            if hand.total > 21:
                hand.state = state.BUST
                break
            decision = Player.act(hand)
            if decision == "stand":
                hand.state = state.STAND

            elif decision == "double":
                # deal only one more card
                hand.cards.append(self.shoe.deal())
                display_cards(hands)
                break

            elif decision == "split":
                card = hand.cards.pop()
                split_hand = Hand(hand.owner)
                split_hand.cards.append(card)
                hands.append(split_hand)
                player_hands.append(split_hand)
                hand.is_splittable = False
                split_hand.is_splittable = False
                display_cards(hands)
                self.play_player_hand(hand, hands, player_hands)

            elif decision == "surrender":
                hand.state = state.SURRENDER
            else:
                hand.cards.append(self.shoe.deal())
                display_cards(hands)

    def play_dealer_hand(self, hands):
        """
        Execute the dealer's sequence of plays

        Dealer mostly keeps hitting till his hand's total is 17 or above it's state is "bust"

        :param hands: All the hands participating in the round
        """
        hand = getDealerHand(hands)
        # Turn dealer second card face up
        hand.cards[1].is_face_up = True
        display_cards(hands)
        # check hand for total greater then 17 or bust
        if hand.total >= 17:
            hand.state = state.STAND
            if hand.total > 21:
                hand.state = state.BUST

        while hand.state == state.IN:
            hand.cards.append(self.shoe.deal())
            display_cards(hands)
            if hand.total > 21:
                hand.state = state.BUST
            elif 17 <= hand.total <= 21:
                hand.state = state.STAND

    @staticmethod
    def getWinners(hands):
        """
        Determine the winning hand

        From the hands provided it determine which hands the won based on the player's hands' total in comparison to
        the dealer's, their states, being blackjack

        :param hands: All hands participating in the round
        :returns winners: list of the winning hands
        """
        dealer = getDealerHand(hands)
        player_hands = getPlayerHands(hands)
        winners = []
        for player in player_hands:
            if dealer.is_blackjack:
                winners.append(dealer.owner.role)
            elif player.is_blackjack:
                winners.append(player.owner.role)
            elif player.state == state.BUST:
                winners.append(dealer.owner.role)
            elif dealer.state == state.BUST:
                winners.append(player.owner.role)
            else:
                # determine winner using hand total
                # highest total wins
                if player.total > dealer.total:
                    winners.append(player.owner.role)
                elif dealer.total > player.total:
                    winners.append(dealer.owner.role)
                else:
                    winners.append("Draw")
        return winners
