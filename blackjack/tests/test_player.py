from blackjack.game.player import Player


class TestPlayer:

    def test_role_defaults_to_player(self):
        assert Player().role == 'Player'
