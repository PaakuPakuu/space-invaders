#!/usr/bin/env python

import pygame
import classes.constants as const
from classes.scene import *

def main():
    """"""
    
    pygame.init()
    window = pygame.display.set_mode((const.SWIDTH, const.SHEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("SPACE INVADERS")
    
    scene = MenuScene(window)

    stop = False
    while not stop:
        action = scene.on_execute()

        if action == const.MAIN_MENU:
            scene = MenuScene(window)
        elif action == const.GAME_MENU:
            scene = GameScene(window)
        elif action == const.OPTION_MENU:
            scene = SettingsScene(window)
        else:
            stop = True

    pygame.quit()
    print('"SPACE INVADERS" @by Jordan HERENG | L2 INF0')

if __name__ == "__main__":
    main()
