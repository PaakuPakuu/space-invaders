import classes.constants as const
from random import randint
from classes.geometry import Point

class Laser:
    """"""

    def __init__(self, sprites, pos):
        """"""

        self.pos = pos
        self._sprites = sprites
        self._currSprite = randint(0, len(sprites) - 1)
        self.has_touched = False

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

    def on_update(self, aliens):
        """"""

        self.pos.y -= const.PLSPEED
        
        if self.pos.y < const.OFFSET_Y or self.collision(aliens):
            self.has_touched = True

    def collision(self, aliens):
        """"""

        for a in aliens:
            if a.rect.contains(self.pos):
                a.take_damage()
                return True
        return False

class LaserAlien(Laser):
    """"""

    def __init__(self, pos):
        """"""

        Laser.__init__(self, const.SPRITES["aliens_lasers"]["laser" + str(randint(1,2))], pos)

        self.__sprite_rate = 100
        self.__next_sprite = 0

    def on_update(self, player, time):
        """"""

        self.pos.y += const.ALSPEED

        if self.pos.y > const.SHEIGHT or self.collisions(player):
            self.has_touched = True
        elif time >= self.__next_sprite:
            self.next_sprite()
            self.__next_sprite = time + self.__sprite_rate

    def collisions(self, player):
        """"""

        pos = Point(self.pos.x + const.MULT, self.pos.y + 5 * const.MULT)
        if player.rect.contains(self.pos) or player.rect.contains(pos):
            player.take_damage()
            return True
        return False
