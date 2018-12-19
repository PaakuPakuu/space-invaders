from random import randint
import classes.constants as const

class Entity:
    """"""

    def __init__(self, pos, sprites):
        """"""

        self.pos = pos
        self.__sprites = sprites
        self.__currentSprite = randint(0, len(self.__sprites) - 1)

    def next_sprite(self):
        """"""

        self.__currentSprite += 1
        if self.__currentSprite >= len(self.__sprites):
            self.__currentSprite = 0

    def on_update(self):
        """"""
        pass

    def on_render(self, surf):
        """"""

        surf.blit(self.__sprites[self.__currentSprite], self.pos.tuple())

class MovingEntity(Entity):
    """"""

    def __init__(self, pos, sprites, speed):
        """"""

        Entity.__init__(self, pos, sprites)
        self.__speed = speed

    def lateral_movement(self, direct):
        """"""

        self.pos.x += self.__speed * direct

class Alien(MovingEntity):
    """"""

    def __init__(self, pos, race):
        """"""

        self.id = race
        MovingEntity.__init__(self, pos, const.SPRITES["alien" + str(race)], const.ASPEED)
        self.__dir = 1

        self.value = race * 10

        self.__sprite_rate = randint(500, 1000)
        self.__next_sprite = 0
    
    def change_dir(self, val):
        """"""

        if val > 0:
            self.__dir = 1
        elif val < 0:
            self.__dir = -1
        else:
            self.__dir = 0

    def update_sprite(self, time):
        """"""

        if time >= self.__next_sprite:
            self.next_sprite()
            self.__next_sprite = time + self.__sprite_rate

    def on_update(self, time):
        """"""

        self.lateral_movement(self.__dir)
        self.update_sprite(time)

class Player(MovingEntity):
    """"""

    pass
