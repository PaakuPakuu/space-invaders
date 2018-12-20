import pygame
from random import randint
import classes.constants as const
from classes.geometry import *
from classes.laser import *

class Entity:
    """"""

    def __init__(self, pos, sprites):
        """"""

        self.pos = pos
        self.__sprites = sprites
        self.__currentSprite = randint(0, len(self.__sprites) - 1)

        width, height = sprites[self.__currentSprite].get_width(), const.EHEIGHT - 2 * const.MULT
        self.rect = Rectangle(pos, width, height)

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

class LivingEntity(Entity):
    """"""

    def __init__(self, pos, sprites, speed, lifes):
        """"""

        Entity.__init__(self, pos, sprites)
        self.__speed = speed
        self.lifes = lifes
        self.alive = True

    def lateral_movement(self, direct):
        """"""

        self.pos.x += self.__speed * direct

    def take_damage(self, val = 1):
        """"""

        self.lifes -= val
        if self.lifes <= 0:
            self.alive = False
            self.lifes = 0

class Alien(LivingEntity):
    """"""

    def __init__(self, pos, place, race):
        """"""

        self.id = race
        LivingEntity.__init__(self, pos, const.SPRITES["alien" + str(race)], const.ASPEED, 1)
        
        self.place = place

        self.__dir = 1

        self.value = race * 10

        self.__sprite_rate = randint(500, 1000)
        self.__next_sprite = 0

        self.__next_fire = 0
        self.__can_shoot = False
    
    def change_dir(self):
        """"""

        self.__dir *= -1

    def update_sprite(self, time):
        """"""

        if time >= self.__next_sprite:
            self.next_sprite()
            self.__next_sprite = time + self.__sprite_rate

    def move_down(self):
        """"""

        self.pos.y += const.STEP_Y

    def shoot(self):
        """"""

        pos = Point(self.pos.x - self.rect.tx() // 2, self.pos.y + self.rect.ty())
        return LaserAlien(pos)

    def on_update(self, time, lasers):
        """"""

        self.lateral_movement(self.__dir)
        self.update_sprite(time)

        if self.__can_shoot and time >= self.__next_fire:
            lasers.append(self.shoot())
            self.__next_fire = time + randint(20, 40) * 100

class Player(LivingEntity):
    """"""

    def __init__(self):
        """"""

        pos = Point((const.SWIDTH - const.EWIDTH) // 2, const.SHEIGHT - const.EHEIGHT - const.OFFSET_Y)
        LivingEntity.__init__(self, pos, const.SPRITES["player"], const.PSPEED, 3)
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

        pos = Point(self.pos.x + const.EWIDTH // 2, self.pos.y)
        self.laser = LaserPlayer(pos)

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
