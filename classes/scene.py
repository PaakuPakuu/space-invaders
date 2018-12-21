import pygame
import classes.constants as const
from classes.hord import Hord
from classes.entities import Player

class Scene:
    """"""

    def __init__(self, window):
        """"""

        self._window = window
        self._running = True
        self._menu_on_quit = const.QUIT

    def on_execute(self):
        """Retourne l'id du menu cible."""

        clock = pygame.time.Clock()

        while self._running:
            # get events
            for e in pygame.event.get():
                self.on_event(e)

            # update
            self.on_update()

            # display
            self._window.fill((0,0,0))
            self.on_render()
            pygame.display.flip()

            clock.tick(50)

        return self._menu_on_quit
# End of Scene class

class MenuScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)
# End of MenuScene class

class GameScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)

        self._on_menu_quit = const.MAIN_MENU
        self.__player = Player()
        self.__hord = Hord(self.__player)

    def on_event(self, event):
        """"""
        if event.type == pygame.QUIT:
            self._running = False
        else:
            self.__player.on_event(event)

    def on_update(self):
        """"""
        self.__hord.on_update(pygame.time.get_ticks())

        if self.__player.laser != None:
            self.__player.laser.on_update(self.__hord)

        self.__player.on_update()

    def on_render(self):
        """"""
        window = self._window

        self.__hord.on_render(window)

        if self.__player.laser != None:
            self.__player.laser.on_render(window)

        self.__player.on_render(window)

# End of GameScene class

class SettingsScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)
# End of SettingsScene class
