import pygame
from random import randint
import classes.constants as const
from classes.geometry import *
from classes.laser import LaserPlayer

class Entity:
    """"""

    def __init__(self, pos, sprites):
        """"""

        self.pos = pos
        self.__sprites = sprites
        self.__currentSprite = randint(0, len(self.__sprites) - 1)
        self.__rect = Rectangle(pos, const.EWIDTH, const.EHEIGHT)

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

        self.__dir *= -1

    def update_sprite(self, time):
        """"""

        if time >= self.__next_sprite:
            self.next_sprite()
            self.__next_sprite = time + self.__sprite_rate

    def on_update(self, time):
        """"""

        self.lateral_movement(self.__dir)
        self.update_sprite(time)

    def move_down(self):
        """"""

        self.pos.y += const.STEP_Y

class Player(MovingEntity):
    """"""

    def __init__(self):
        """"""

        pos = Point((const.SWIDTH - const.EWIDTH) // 2, const.SHEIGHT - const.EHEIGHT - const.OFFSET_Y)
        MovingEntity.__init__(self, pos, const.SPRITES["player"], const.PSPEED)
        self.__currentSprite = 0

        self.__velocity = 0

        self.laser = None

    def move(self, event):
        """"""

        if event.key == pygame.K_LEFT:
            self.__velocity -= 1
        elif event.key == pygame.K_RIGHT:
            self.__velocity += 1

    def stop_moving(self, event):
        """"""

        if event.key == pygame.K_LEFT:
            self.__velocity += 1
        elif event.key == pygame.K_RIGHT:
            self.__velocity -= 1

    def replace(self):
        """"""

        if self.pos.x < const.BORDER_LEFT:
            self.pos.x = const.BORDER_LEFT
        elif self.pos.x > const.BORDER_RIGHT:
            self.pos.x = const.BORDER_RIGHT

    def shoot(self):
        """"""

        self.laser = LaserPlayer(Point(self.pos.x + const.EWIDTH // 2, self.pos.y))

    def on_event(self, event):
        """"""

        if event.type == pygame.KEYDOWN:
            self.move(event)
            
            if self.laser == None and event.key == pygame.K_SPACE:
                self.shoot()
        elif event.type == pygame.KEYUP:
            self.stop_moving(event)

    def on_update(self):
        """"""

        self.lateral_movement(self.__velocity)
        self.replace()

        if self.laser != None and self.laser.has_touched:
            self.laser = None
