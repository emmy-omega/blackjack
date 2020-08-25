import click
from pyfiglet import Figlet

from .game.Shoe import Shoe
from blackjack.game.game import Game
from blackjack.game.player import Player


@click.command()
@click.option("--rounds", "-r", default=1, help="How many round of the game to play, default is 1")
def run(rounds=1):
    rounds = int(rounds)
    players = [Player(role="Dealer"), Player(role="Player")]
    game = Game(players, Shoe())
    for i in range(rounds):
        hands = game.start_round
        winners = Game.getWinners(hands)
        displayResult(winners)


def displayResult(winners):
    # print(winners)
    f = Figlet(font='slant')
    if "Player" in winners:
        print(f.renderText('Player Wins'))
    else:
        print(f.renderText('Dealer Wins'))
