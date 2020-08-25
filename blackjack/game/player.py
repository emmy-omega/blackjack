from __future__ import print_function, unicode_literals

from PyInquirer import prompt
from examples import custom_style_2

from blackjack.common.constants import role as r


class Player:
    """
    Class presenting participants of the game

    Attributes
    ----------
    role: str
        The role to played in the game

    Methods
    -------
    act()
        Retrieves player choice of action
    """
    def __init__(self, role=r.PLAYER):
        self.role = role

    @staticmethod
    def act(hand):
        """
        Prompt the player for an action for the provided choices

        :param hand: The hand on which the action chosen will be executing
        :return: action: The action chosen by the player
        """
        choices = ['hit', 'stand']

        if hand.is_splittable:
            choices.append("split")
        if len(hand.cards) == 2:
            choices.append("double")
            choices.append("surrender")

        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'What do you want to do?',
                'choices': choices
            }
        ]

        return prompt(questions, style=custom_style_2).get('action', 'hit')
