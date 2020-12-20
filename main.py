"""Greeter.

Usage:
  main.py --inside
  main.py --cover
  main.py --card
  main.py -h | --help

Options:
  -h --help     Show this screen.
"""

# built in
import os


# third party
from docopt import docopt

# project based
from card import card_graphics as cg
from card import card_inside as ci


if __name__ == '__main__':
    cli_arguments = docopt(__doc__)
    user = str(os.getlogin()).replace('.', ' ').capitalize()
    if cli_arguments.get('--cover', True):
        cg.Card().build_cover()

    if cli_arguments.get('--inside', True):
        ci.InternalCard().build_internal(user)

    if cli_arguments.get('--card', True):
        cg.Card().build_cover()
        ci.InternalCard().build_internal(user)
