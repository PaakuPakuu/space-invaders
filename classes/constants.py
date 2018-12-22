import pygame

MULT = 3

# Screen
SWIDTH, SHEIGHT = 224 * MULT, 256 * MULT
SRECT = (SWIDTH, SHEIGHT)
OFFSET_X, OFFSET_Y = 5 * MULT, 35 * MULT

# Menus ID
QUIT = -1
MAIN_MENU = 0
GAME_MENU = 1
OPTION_MENU = 2

# Entities settings
EWIDTH, EHEIGHT = 12 * MULT, 8 * MULT
BORDER_LEFT, BORDER_RIGHT = OFFSET_X, SWIDTH - OFFSET_X - EWIDTH

# Hord settings
ROWS, COLUMNS = 5, 11
SPACE_X, SPACE_Y = EWIDTH + 4 * MULT, EHEIGHT + 6 * MULT
SPACE_BONUS = 40 * MULT
STEP_Y = 3 * MULT

NB_ALIENS_TYPE = 3

# Aliens settings
FIRST = 1
SECOND = 2
THIRD = 3

ASPEED = 0.1 * MULT
ALSPEED = 2.5 * MULT

# Player settings
PSPEED = 2 * MULT
PLSPEED = 6 * MULT

# Sprites name
def load_sprites():
    """"""
    
    sprites = {}
    path = "./resources/images/"

    def convert_image(path):
        """"""

        image = pygame.image.load(path)
        image.set_colorkey((255,0,255))
        image = pygame.transform.scale(image, (image.get_width() * MULT, image.get_height() * MULT))

        return image

    # aliens sprites
    for i in range(NB_ALIENS_TYPE):
        name = "alien" + str(i + 1)
        images = []
        for j in range(2):
            images.append(convert_image(path + "aliens/" + name + "/" + str(j) + ".png"))
        sprites[name] = images

    # aliens lasers sprites
    sprites["aliens_lasers"] = {}
    for i in range(2):
        name = "laser" + str(i + 1)
        lasers = []
        for j in range(3):
            lasers.append(convert_image(path + "aliens/lasers/" + name + "/laser_" + str(j + 1) + ".png"))
        sprites["aliens_lasers"][name] = lasers

    # player sprites
    sprites["player"] = []
    for n in ["normal", "destroyed"]:
        sprites["player"].append(convert_image(path + "player/" + n + ".png"))

    # player lasers sprites
    sprites["player_lasers"] = [convert_image(path + "player/lasers/laser.png")]

    # explosions sprites
    sprites["explosion"] = [convert_image(path + "explosion/" + str(name) + ".png") for name in range(3)]

    return sprites

SPRITES = load_sprites()

# GUI settings
COLOR = (255,255,255)

SCOREP1_POS1, SCOREP1_POS2 = (15 * MULT, 5 * MULT), (25 * MULT, 15 * MULT)
HISCORE_POS1, HISCORE_POS2 = (92 * MULT, 5 * MULT), (102 * MULT, 15 * MULT)
SCOREP2_POS1, SCOREP2_POS2 = (165 * MULT, 5 * MULT), (175 * MULT, 15 * MULT)

BEGIN_LINE, END_LINE = (0, SHEIGHT - 15 * MULT), (SWIDTH, SHEIGHT - 15 * MULT)

TEXT_LIFE_POS = (10 * MULT, SHEIGHT - 14 * MULT)
LIFE_POS = (25 * MULT, SHEIGHT - 12 * MULT)
LIFE_SPACE = EWIDTH + 4 * MULT

CREDIT_POS = (SWIDTH - 50 * MULT, SHEIGHT - 14 * MULT)
