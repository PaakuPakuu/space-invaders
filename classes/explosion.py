from classes.constants import SPRITES, MULT

NOBODY = -1
PLAYER = 0
ALIEN = 1
LASER = 2

class Explosion:
    """"""

    def __init__(self, pos, t, time):
        """"""
        
        self.__pos = pos
        self.__sprite = SPRITES["explosion"][t]

        self.destroy = False
        self.__time_destroy = time + 100

    def on_update(self, time):
        """"""

        if time >= self.__time_destroy:
            self.destroy = True

    def on_render(self, surf):
        """"""

        surf.blit(self.__sprite, (self.__pos.x - self.__sprite.get_width() // 2, self.__pos.y - 2 * MULT))
