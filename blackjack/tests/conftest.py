import pytest

from blackjack.game.Shoe import Shoe
from blackjack.common.constants import role
from blackjack.game.game import Game
from blackjack.game.hand import Hand
from blackjack.game.player import Player


@pytest.fixture
def player():
    return Player()


@pytest.fixture
def dealer():
    return Player(role.DEALER)


@pytest.fixture
def hand(player):
    return Hand(owner=player)


@pytest.fixture
def dealer_hand():
    return Hand(Player(role.DEALER))


@pytest.fixture
def shoe():
    return Shoe()


@pytest.fixture
def game(shoe, dealer, player):
    return Game([dealer, player], shoe)
