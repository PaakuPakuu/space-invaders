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
        self.font = pygame.font.Font("./resources/fonts/text.ttf", 15 * const.MULT)

        self.__t_score1_p1 = self.font.render("SCORE<1>", False, const.COLOR)
        self.__t_score2_p1 = self.font.render("0000", False, const.COLOR)

        self.__t_hiscore1 = self.font.render("HI-SCORE", False, const.COLOR)
        self.__t_hiscore2 = self.font.render("0000", False, const.COLOR)

        self.__t_score1_p2 = self.font.render("SCORE<2>", False, const.COLOR)
        self.__t_score2_p2 = self.font.render("0000", False, const.COLOR)

        self.__t_lifes = self.font.render("0", False, const.COLOR)
        self.__life_sprite = const.SPRITES["player"][0]

        self.__t_credits = self.font.render("CREDIT 00", False, const.COLOR)

    def convert_score(self, n, t):
        """"""

        return (t - len(str(n))) * "0" + str(n)

    def on_update(self):
        """"""

        self.__t_score2_p1 = self.font.render(self.convert_score(self.score, 4), False, const.COLOR)
        self.__t_hiscore2 = self.font.render(self.convert_score(self.hiscore, 4), False, const.COLOR)

        self.__t_lifes = self.font.render(str(self.lifes), False, const.COLOR)
        self.__t_credits = self.font.render("CREDIT " + self.convert_score(self.credits, 2), False, const.COLOR)

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

        for i in range(self.lifes - 1):
            x, y = const.LIFE_POS
            surf.blit(self.__life_sprite, (x + i * const.LIFE_SPACE, y))
        
        surf.blit(self.__t_credits, const.CREDIT_POS)

# End of GUI class

def on_middle(surf):
    """"""

    return (const.SWIDTH - surf.get_width()) // 2
