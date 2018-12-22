import pygame
import classes.constants as const

class GUI:
    """"""

    def __init__(self):
        """"""
        
        self.score = self.hiscore = 0
        self.lifes = 0
        self.credits = 0
        
        # sprites and texts
        self.__font = pygame.font.Font("resources/fonts/text.ttf", const.FONT_SIZE)
        self.__color = (255,255,255)

        self.__t_score1_p1 = self.__font.render("SCORE<1>", False, self.__color)
        self.__t_score2_p1 = self.__font.render("0000", False, self.__color)

        self.__t_hiscore1 = self.__font.render("HI-SCORE", False, self.__color)
        self.__t_hiscore2 = self.__font.render("0000", False, self.__color)

        self.__t_score1_p2 = self.__font.render("SCORE<2>", False, self.__color)
        self.__t_score2_p2 = self.__font.render("0000", False, self.__color)

        self.__t_lifes = self.__font.render("0", False, self.__color)
        self.__life_sprite = const.SPRITES["player"][0]

        self.__t_credits = self.__font.render("CREDIT 00", False, self.__color)

    def convert_score(self, n, t):
        """"""

        return (t - len(str(n))) * "0" + str(n)

    def on_update(self):
        """"""

        self.__t_score2_p1 = self.__font.render(self.convert_score(self.score, 4), False, self.__color)
        self.__t_hiscore2 = self.__font.render(self.convert_score(self.hiscore, 4), False, self.__color)

        self.__t_lifes = self.__font.render(str(self.lifes), False, self.__color)
        self.__t_credits = self.__font.render("CREDIT " + self.convert_score(self.credits, 2), False, self.__color)

    def on_render(self, surf):
        """"""

        surf.blit(self.__t_score1_p1, const.SCOREP1_POS1)
        surf.blit(self.__t_score2_p1, const.SCOREP1_POS2)

        surf.blit(self.__t_hiscore1, const.HISCORE_POS1)
        surf.blit(self.__t_hiscore2, const.HISCORE_POS2)

        surf.blit(self.__t_score1_p2, const.SCOREP2_POS1)
        surf.blit(self.__t_score2_p2, const.SCOREP2_POS2)

        if self.lifes > 0:
            surf.blit(self.__t_lifes, const.TEXT_LIFE_POS)

        for i in range(self.lifes):
            x, y = const.LIFE_POS
            surf.blit(self.__life_sprite, (x + i * const.LIFE_SPACE, y))
        
        surf.blit(self.__t_credits, const.CREDIT_POS)

# End of GUI class

def on_middle(surf):
    """"""

    return (const.SWIDTH - surf.get_width()) // 2
