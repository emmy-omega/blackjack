from collections import namedtuple
from rich.console import Console

state = namedtuple('State', ['BUST', 'IN', 'STAND', 'SURRENDER'], defaults=['bust', 'in', 'stand', 'surrender'])()
role = namedtuple('Role', ['PLAYER', 'DEALER'], defaults=['Player', 'Dealer'])()
console = Console()