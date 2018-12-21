import pygame
import classes.constants as const

class GUI:
    """"""

    def __init__(self):
        """"""
        
        self.score = self.hiscore = 0
        self.lifes = 3
        
        # sprites and texts
        self.__font = pygame.font.Font("resources/fonts/text.ttf", const.FONT_SIZE)
        self.__color = (255,255,255)

        self.__t_score1 = self.__font.render("SCORE<1>", False, self.__color)
        self.__t_score2 = self.__font.render("0", False, self.__color)

        self.__t_hiscore1 = self.__font.render("HI-SCORE", False, self.__color)
        self.__t_hiscore2 = self.__font.render("0", False, self.__color)

        self.__t_lifes = self.__font.render("0", False, self.__color)
        self.__life_sprite = const.SPRITES["player"][0]

    def on_update(self):
        """"""

        self.__t_score2 = self.__font.render(str(self.score), False, self.__color)
        self.__t_hiscore2 = self.__font.render(str(self.hiscore), False, self.__color)

        self.__t_lifes = self.__font.render(str(self.lifes), False, self.__color)

    def on_render(self, surf):
        """"""

        surf.blit(self.__t_score1, const.SCORE_POS1)
        surf.blit(self.__t_score2, const.SCORE_POS2)

        surf.blit(self.__t_hiscore1, const.HISCORE_POS1)
        surf.blit(self.__t_hiscore2, const.HISCORE_POS2)

        # green line
        pygame.draw.line(surf, (0,255,0), const.BEGIN_LINE, const.END_LINE, const.MULT)

        surf.blit(self.__t_lifes, const.TEXT_LIFE_POS)

        for i in range(self.lifes):
            x, y = const.LIFE_POS
            surf.blit(self.__life_sprite, (x + i * const.LIFE_SPACE, y))
