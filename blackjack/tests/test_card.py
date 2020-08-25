import pytest

from blackjack.game.card import Card


class TestCard:

    def test_faced_by_default(self):
        card = Card.generate('T')
        assert card.is_face_up

    @pytest.mark.parametrize('rank', ['T', 'J', 'Q', 'K'])
    def test_high_cards_weigh_10(self, rank):
        assert Card.generate(rank).weight == 10

    @pytest.mark.parametrize('rank', [str(r) for r in range(2, 10)])
    def test_ranks_9_or_less_weight_rank(self, rank):
        assert Card.generate(rank).weight == int(rank)

    def test_rank_A_weight_11(self):
        assert Card.generate('A').weight == 1

    @pytest.mark.parametrize('rank', [str(r) for r in range(2, 7)])
    def test_ranks_6_or_less_value_negative_1(self, rank):
        assert Card.generate(rank).value == -1

    @pytest.mark.parametrize('rank', ['7', '8', '9'])
    def test_ranks_7_to_9_value_0(self, rank):
        assert Card.generate(rank).value == 0

    @pytest.mark.parametrize('rank', ['T', 'J', 'Q', 'K'])
    def test_high_ranks_value_1(self, rank):
        assert Card.generate(rank).value == 1

    @pytest.mark.parametrize('rank', Card.ranks[-5:])
    def test_type_is_high(self,rank):
        assert Card.generate(rank).type == 'high'

    @pytest.mark.parametrize('rank', Card.ranks[:8])
    def test_type_is_low(self, rank):
        assert Card.generate(rank).type == 'low'


# if __name__ == '__main__':
#     unittest.main()
