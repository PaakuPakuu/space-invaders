import classes.constants as const
from random import randint
from classes.geometry import *
from classes.explosion import *

class Laser:
    """"""

    def __init__(self, sprites, pos):
        """"""

        self.pos = pos
        self._sprites = sprites
        self._currSprite = randint(0, len(sprites) - 1)
        self.has_touched = NOBODY

    def next_sprite(self):
        """"""

        self._currSprite += 1
        if self._currSprite == len(self._sprites):
            self._currSprite = 0

    def on_render(self, surf):
        """"""

        surf.blit(self._sprites[self._currSprite], self.pos.tuple())
    
class LaserPlayer(Laser):
    """"""

    def __init__(self, pos):
        """"""

        Laser.__init__(self, const.SPRITES["player_lasers"], pos)

    def on_update(self, hord):
        """"""

        self.pos.y -= const.PLSPEED
        
        if self.pos.y < const.OFFSET_Y:
            self.has_touched = LASER
        else:
            self.has_touched = self.collision(hord)

    def collision(self, hord):
        """"""

        for a in hord.aliens:
            if a.rect.contains(self.pos) or a.rect.contains(Point(self.pos.x + const.MULT, self.pos.y)):
                a.take_damage()
                return ALIEN

        for l in hord.lasers:
            if l.rect.contains(self.pos):
                l.has_touched = LASER
                return LASER
        return NOBODY

class LaserAlien(Laser):
    """"""

    def __init__(self, pos):
        """"""

        Laser.__init__(self, const.SPRITES["aliens_lasers"]["laser" + str(randint(1,2))], pos)

        self.rect = Rectangle(self.pos, 3 * const.MULT, 4 * const.MULT)

        self.__sprite_rate = 100
        self.__next_sprite = 0

    def on_update(self, player, time):
        """"""

        self.pos.y += const.ALSPEED

        if self.pos.y >= const.BEGIN_LINE[1] - 5 * const.MULT:
            self.has_touched = LASER
        else:
            self.has_touched = self.collisions(player, time)

        if time >= self.__next_sprite:
            self.next_sprite()
            self.__next_sprite = time + self.__sprite_rate

    def collisions(self, player, time):
        """"""

        if not player.dead and player.rect.intersects(self.rect):
            player.take_damage()
            player.dead = True
            player.dead_time = time + 1500
            player.laser = None

            return PLAYER
        return NOBODY
