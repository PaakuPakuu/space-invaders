import classes.constants as const
from random import randint

class Laser:
    """"""

    def __init__(self, sprites, pos):
        """"""

        self.pos = pos
        self._sprites = sprites
        self._currSprite = randint(0, len(sprites) - 1)
        self.has_touched = False

    def on_render(self, surf):
        """"""

        surf.blit(self._sprites[self._currSprite], self.pos.tuple())
    
class LaserPlayer(Laser):
    """"""

    def __init__(self, pos):
        """"""

        Laser.__init__(self, const.SPRITES["player_lasers"], pos)

    def on_update(self):
        """"""

        self.pos.y -= const.PLSPEED
        
        if self.pos.y < const.OFFSET_Y:
            self.has_touched = True

class LaserAlien(Laser):
    """"""

    def __init__(self, pos):
        """"""

        Laser.__init__(self, SPRITES["aliens_lasers"][str(randint(1,2))], pos)

    def on_update(self):
        """"""

        self.pos.y += ALSPEED

        if self.pos.y > const.SHEIGHT:
            self.has_touched = True
