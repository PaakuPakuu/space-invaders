import classes.constants as const
from classes.entities import Alien

class SpaceInvaders:
    """"""

    def __init__(self, rows=const.ROWS, cols=const.COLUMNS):
        """"""

        self.__aliens = init_aliens(rows, cols)

    def __str__(self):
        """temp"""

        ch = ""

        for r in self.__aliens:
            for c in r:
                ch += str(c.id) + " "
            ch += "\n"

        return ch
#

def init_aliens(r, c):
    """"""

    # A revoir pour généraliser
    # pistes
    # → si r impair, terminer par 1 THIRD
    # → si r pair, terminer par 1 SECOND puis 1 THIRD

    aliens = 2 * [c * [Alien(None, const.THIRD)]]
    aliens += 2 * [c * [Alien(None, const.SECOND)]]
    aliens += [c * [Alien(None, const.FIRST)]]

    return aliens
