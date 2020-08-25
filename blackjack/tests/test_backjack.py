from blackjack.game.card import Card
from blackjack.game.game import Game


class TestBlackjack:

    def test_dealer_win_with_higher_total(self, mocker, game, dealer_hand, hand):
        dealer_hand.cards = [Card('T'), Card('Q')]
        hand.cards = [Card('T'), Card('8')]

        def mock_start_round(self):
            return [dealer_hand, hand]

        mocker.patch(
            'blackjack.blackjack.Game.start_round',
            mock_start_round
        )
        winners = Game.getWinners(game.start_round)
        assert 'Dealer' in winners

    def test_draw_on_equal_totals(self, mocker, game, dealer_hand, hand):
        dealer_hand.cards = [Card('4'), Card('3'), Card('3'), Card('7')]
        hand.cards = [Card('3'), Card('A'), Card('T'), Card('3')]

        def mock_start_round(self):
            return [dealer_hand, hand]

        mocker.patch(
            'blackjack.blackjack.Game.start_round',
            mock_start_round
        )
        winners = Game.getWinners(game.start_round)
        assert 'Draw' in winners
