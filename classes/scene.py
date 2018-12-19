import pygame
import classes.constants as const

class Scene:
    """"""

    def __init__(self, window):
        """"""

        self.__window = window
        self.__running = True
        self.__menu_on_quit = const.GAME_MENU

    def on_event(self, event):
        """"""

        if event.type == pygame.QUIT:
            self.__running = False

    def on_update(self):
        """"""

        pass

    def on_render(self):
        """"""

        pass

    def on_execute(self):
        """Retourne l'id du menu cible."""

        while self.__running:
            # get events
            for e in pygame.event.get():
                self.on_event(e)

            # update
            self.on_update()

            # display
            self.on_render()

        return self.__menu_on_quit
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
# End of GameScene class

class SettingsScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)
# End of SettingsScene class
