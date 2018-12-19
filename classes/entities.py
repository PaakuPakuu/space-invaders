class Entity:
    """"""

    def __init__(self, pos, sprites):
        """"""

        self.__pos = pos
        self.__sprites = sprites

    def on_update(self):
        """"""
        pass


class MovingEntity(Entity):
    """"""

    def __init__(self, pos, sprites, speed):
        """"""

        Entity.__init__(self, pos, sprites)
        self.__speed = speed

class Alien(MovingEntity):
    """"""

    def __init__(self, pos, race):
        """"""

        self.id = race

        # set sprites and speed depending to the race
        MovingEntity.__init__(self, pos, None, None)
