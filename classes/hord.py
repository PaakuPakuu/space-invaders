import classes.constants as const
from classes.entities import Alien
from classes.geometry import Point

class Hord:
    """"""

    def __init__(self, rows=const.ROWS, cols=const.COLUMNS):
        """"""

        self.__aliens = init_aliens(rows, cols)
        self.__pos = self.__aliens[0][0].pos
    
    def on_border_left(self):
        """"""

        return self.__pos.x < const.OFFSET_X

    def on_border_right(self):
        """"""

        return self.__pos.x + const.TX > const.SWIDTH - const.OFFSET_X

    def on_update(self, time):
        """"""

        for row in self.__aliens:
            for alien in row:
                alien.on_update(time)
                if self.on_border_left() or self.on_border_right():
                    alien.change_dir(1)
                    alien.move_down()

    def on_render(self, surf):
        """"""

        for row in self.__aliens:
            for alien in row:
                alien.on_render(surf)

# End of SpaceInvaders class

def init_aliens(r, c):
    """"""

    # A revoir pour généraliser
    # pistes
    # → si r impair, terminer par 1 THIRD
    # → si r pair, terminer par 1 SECOND puis 1 THIRD

    aliens = []

    for i in range(r):
        row = []
        for j in range(c):
            pos = Point(const.OFFSET_X + j * const.SPACE_X, const.OFFSET_Y + i * const.SPACE_Y)
            race = 0
            if i < 2:
                race = const.THIRD
            elif 2 <= i <= 3:
                race = const.SECOND
            else:
                race = const.FIRST

            row.append(Alien(pos, race))
        aliens.append(row)

    return aliens