import classes.constants as const
from classes.entities import Alien
from classes.geometry import Point
from random import randint

class Hord:
    """"""

    def __init__(self, player, rows=const.ROWS, cols=const.COLUMNS):
        """"""

        self.aliens = init_aliens(rows, cols)
        self.__pos = self.aliens[0].pos
        self.__down = 0
        self.nb_aliens = rows * cols

        self.__min_col, self.__max_col = 0, cols - 1
        self.__max_row = rows - 1
        self.__rows = rows
        self.__cols = self.__max_col - self.__min_col

        self.__lasers = []
        self.__player = player
    
    def on_border_left(self):
        """"""

        return self.__pos.x < const.BORDER_LEFT

    def on_border_right(self):
        """"""

        return self.__pos.x + self.__cols * const.SPACE_X > const.BORDER_RIGHT

    def reset_cols(self):
        """"""
        
        mini = maxi = self.aliens[0].place.x
        for a in self.aliens:
            col = a.place.x
            if col > maxi:
                maxi = col
            elif col < mini:
                mini = col

        self.__min_col = mini
        self.__max_col = maxi
        self.__cols = maxi - mini

    def reset_rows(self):
        """"""

        maxi = self.aliens[0].place.y
        for a in self.aliens:
            row = a.place.y
            if row > maxi:
                maxi = row

        self.__max_row = maxi

    def reset_pos(self):
        """"""

        i = 0
        trouve = False
        while not trouve and i < self.nb_aliens:
            a = self.aliens[i]
            if a.place.x == self.__min_col:
                self.__pos = a.pos
                trouve = True
            i += 1

    def allow_shoot(self, x, time):
        """"""

        ind_max = i = 0
        while i < self.nb_aliens:
            a = self.aliens[i]
            if a.place.x == x and a.place.y > self.aliens[ind_max].place.y:
                ind_max = i
            i += 1

        self.aliens[ind_max].can_shoot = True
        self.aliens[ind_max].next_fire = time + randint(10, 100) * 100

    def on_update(self, time):
        """"""

        # update aliens
        i = 0
        while i < self.nb_aliens:
            alien = self.aliens[i]

            if alien.alive:
                alien.on_update(time, self.__lasers)

                if self.on_border_left() or self.on_border_right():
                    alien.change_dir()
                    alien.move_down()
                    self.__down += 1

                i += 1
            else:
                x = alien.place.x
                del(self.aliens[i])
                self.nb_aliens -= 1
                self.allow_shoot(x, time)
                
                self.reset_cols()
                self.reset_rows()
                self.reset_pos()

        # update lasers
        i = 0
        while i < len(self.__lasers):
            laser = self.__lasers[i]
            if laser.has_touched:
                del(self.__lasers[i])
            else:
                laser.on_update(self.__player, time)
                i += 1

    def on_render(self, surf):
        """"""

        # display aliens
        for alien in self.aliens:
            alien.on_render(surf)

        # display lasers
        for laser in self.__lasers:
            laser.on_render(surf)

# End of SpaceInvaders class

def init_aliens(r, c):
    """"""

    # A revoir pour généraliser
    aliens = []

    for i in range(r):
        for j in range(c):
            x = const.OFFSET_X + j * const.SPACE_X
            y = const.OFFSET_Y + const.SPACE_BONUS + i * const.SPACE_Y
            pos = Point(x, y)
            race = 0
            if i < 2:
                race = const.THIRD
            elif 2 <= i <= 3:
                race = const.SECOND
            else:
                race = const.FIRST

            aliens.append(Alien(pos, Point(j, i), race, i == r - 1))

    return aliens
