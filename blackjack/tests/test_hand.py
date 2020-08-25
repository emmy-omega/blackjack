import pytest

from blackjack.game.card import Card
from blackjack.game.hand import Hand


class TestHand:

    def test_split_return_new_player_owned_instance(self, hand, player):
        split_hand = hand.split()
        assert type(split_hand) is Hand
        assert split_hand.owner == player

    @pytest.mark.parametrize('pair, totals', [(['T', '8'], (18, 0)), (['A', '8'], (9, 19))])
    def test_totals(self, hand, pair, totals):
        rank1, rank2 = pair
        hand.cards.append(Card.generate(rank1))
        hand.cards.append(Card.generate(rank2))
        assert hand.totals == totals

    def test_is_soft(self, player):
        hand = Hand(player)
        ace = Card.generate('A')
        hand.cards.append(ace)
        hand.cards.append(Card.generate('9'))
        assert hand.is_soft
        hand.cards.remove(ace)
        hand.cards.append(Card.generate('T'))
        assert not hand.is_soft

    def test_non_aced_is_hard(self, player):
        hand = Hand(player)
        hand.cards.append(Card.generate('T'))
        hand.cards.append(Card.generate('T'))
        assert not hand.is_soft

    def test_is_paired(self, player):
        hand = Hand(player)
        hand.cards.append(Card.generate('T'))
        hand.cards.append(Card.generate('T'))
        assert hand.is_paired
        hand.cards.pop()
        hand.cards.append(Card.generate('8'))
        assert not hand.is_paired

    @pytest.mark.parametrize('sec_hand', ['T', 'J', 'Q', 'K'])
    def test_is_blackjack(self, player, sec_hand):
        hand = Hand(player)
        ace = Card.generate('A')
        hand.cards.append(ace)
        hand.cards.append(Card.generate(sec_hand))
        assert len([c for c in hand.cards if c.type == 'high']) == 2
        assert hand.is_soft
        assert hand.is_blackjack

    def test_aces_not_blackjack(self, player):
        hand = Hand(player)
        hand.cards.append(Card.generate('A'))
        hand.cards.append(Card.generate('A'))
        assert not hand.is_blackjack
