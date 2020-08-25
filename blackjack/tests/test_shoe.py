import pytest

from blackjack.game.Shoe import Shoe
from blackjack.game.card import Card


class TestShoe:

    @pytest.mark.parametrize('decks', [1, 2, 3])
    def test_generates_card(self, decks):
        shoe = Shoe(decks=decks)
        assert type(shoe.cards) is list
        assert len(shoe.cards) == 52 * decks

    def test_shuffles_card(self):
        shoe = Shoe()
        unshuffled = shoe.cards.copy()
        shoe.shuffle()
        shuffled = shoe.cards
        assert unshuffled != shuffled

    def test_deal_deals_a_card(self):
        shoe = Shoe()
        cards = shoe.cards
        card = shoe.deal()
        assert type(card) is Card

    def test_card_less_after_deal(self):
        shoe = Shoe()
        cards_len = len(shoe.cards) - 1
        shoe.deal()
        assert cards_len == len(shoe.cards)

    def test_deal_returns_a_card(self):
        shoe = Shoe()
        assert type(shoe.deal()) is Card
