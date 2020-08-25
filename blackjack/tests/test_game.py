import pytest

from blackjack.game.Shoe import Shoe
from blackjack.game.card import Card
from blackjack.game.game import Game
from blackjack.game.player import Player


class TestGame:

    def test_moreThan1_dealer_raises_ValueErr(self):
        player0 = Player(role="Dealer")
        player1 = Player(role="Dealer")
        player2 = Player(role="Player")
        players = [player0, player1, player2]
        shoe = Shoe(1)
        with pytest.raises(ValueError):
            Game(players, shoe)

    def test_getWinners_returns_list_winning_hands(self, dealer_hand, hand):
        dealer_hand.cards = [Card.generate('A'), Card.generate('T')]
        hand.cards = [Card.generate('T'), Card.generate('T')]
        hands = [dealer_hand, hand]
        winners = Game.getWinners(hands)
        assert type(winners) is list
        assert "Dealer" in winners
