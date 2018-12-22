import pygame
import classes.constants as const
from classes.hord import Hord
from classes.entities import Player
from classes.gui import *

class Scene:
    """"""

    def __init__(self, window):
        """"""

        self._window = window
        self._running = True
        self.__menu_on_quit = const.QUIT
        self._gui = GUI()

    def set_next_scene(self, name):
        """"""

        self.__menu_on_quit = name

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

        return self.__menu_on_quit
# End of Scene class

class MenuScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)

        # sprites and texts
        self.__font = pygame.font.Font("resources/fonts/text.ttf", const.FONT_SIZE)
        self.__color = (255,255,255)

        self.__t_play = self.__font.render("PLAY", False, self.__color)

        logo = pygame.image.load("./resources/images/logo.png")
        logo.set_colorkey((255,0,255))
        self.__logo = pygame.transform.scale(logo, (100 * const.MULT, 50 * const.MULT))

        self.__t_sat = self.__font.render("*SCORE ADVANCE TABLE*", False, self.__color)
        self.__t_mystery = self.__font.render("=? MYSTERY", False, (255,0,0))
        self.__t_30 = self.__font.render("=30 POINTS", False, self.__color)
        self.__t_20 = self.__font.render("=20 POINTS", False, self.__color)
        self.__t_10 = self.__font.render("=10 POINTS", False, self.__color)

    def on_event(self, event):
        """"""

        if event.type == pygame.QUIT:
            self.set_next_scene(const.QUIT)
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.key == pygame.K_RETURN:
                self.set_next_scene(const.GAME_MENU)
                self._running = False

    def on_update(self):
        """"""

        # faire apparaître petit à petit le texte
        pass

    def on_render(self):
        """"""

        window = self._window

        self._gui.on_render(window)
        window.blit(self.__logo, (on_middle(self.__logo), 70 * const.MULT))

        window.blit(self.__t_play, (on_middle(self.__t_play), 50 * const.MULT))
        window.blit(self.__t_sat, (on_middle(self.__t_sat),  130 * const.MULT))

        window.blit(self.__t_mystery, (on_middle(self.__t_mystery) + 10,  145 * const.MULT))
        window.blit(self.__t_30, (on_middle(self.__t_30) + 10,  160 * const.MULT))
        window.blit(self.__t_20, (on_middle(self.__t_20) + 10,  175 * const.MULT))
        window.blit(self.__t_10, (on_middle(self.__t_10) + 10,  190 * const.MULT))

        sprites = [const.SPRITES["alien3"][0], const.SPRITES["alien2"][0], const.SPRITES["alien1"][0]]
        window.blit(sprites[0], (on_middle(self.__t_30) - 7 * const.MULT, 162 * const.MULT))
        window.blit(sprites[1], (on_middle(self.__t_20) - 10 * const.MULT, 177 * const.MULT))
        window.blit(sprites[2], (on_middle(self.__t_10) - 11 * const.MULT, 192 * const.MULT))

# End of MenuScene class

class GameScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)

        self.__player = Player()
        self.__hord = Hord(self.__player)

        self.__won = False

    def on_event(self, event):
        """"""
        if event.type == pygame.QUIT:
            self.set_next_scene(const.QUIT)
            self._running = False
        else:
            self.__player.on_event(event)

    def on_update(self):
        """"""

        self._gui.on_update()
        
        time = pygame.time.get_ticks()

        self.__hord.on_update(time, self._gui)

        if self.__player.laser != None:
            self.__player.laser.on_update(self.__hord)
        if self.__player.explosion != None:
            self.__player.explosion.on_update(time)

        self.__player.on_update(time, self._gui)

        if not self.__player.alive or self.__hord.nb_aliens == 0:
            self._running = False
            if self.__player.alive:
                self.__won = True
            self.set_next_scene(const.MAIN_MENU)

    def on_render(self):
        """"""

        window = self._window

        self._gui.on_render(window)
        pygame.draw.line(window, (0,255,0), const.BEGIN_LINE, const.END_LINE, const.MULT)

        self.__hord.on_render(window)

        if self.__player.laser != None:
            self.__player.laser.on_render(window)
        if self.__player.explosion != None:
            self.__player.explosion.on_render(window)

        self.__player.on_render(window)

# End of GameScene class

class SettingsScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)
# End of SettingsScene class
