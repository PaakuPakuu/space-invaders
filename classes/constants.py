import pygame

MULT = 3

# Screen
SWIDTH, SHEIGHT = 224 * MULT, 256 * MULT
SRECT = (SWIDTH, SHEIGHT)
OFFSET_X, OFFSET_Y = 5 * MULT, 30 * MULT

# Menus ID
QUIT = -1
MAIN_MENU = 0
GAME_MENU = 1
OPTION_MENU = 2

# Entities settings
EWIDTH, EHEIGHT = 12 * MULT, 8 * MULT

# Hord settings
ROWS, COLUMNS = 5, 11
SPACE_X, SPACE_Y = EWIDTH + 4 * MULT, EHEIGHT + 4 * MULT
TX, TY = ROWS * (EWIDTH + SPACE_X), COLUMNS * (EHEIGHT + SPACE_Y)

NB_ALIENS_TYPE = 3

# Aliens settings
FIRST = 1
SECOND = 2
THIRD = 3

ASPEED = 0.1 * MULT

# Sprites name

def load_sprites():
    """"""
    
    sprites = {}
    path = "./resources/images/"
    for i in range(NB_ALIENS_TYPE):
        name = "alien" + str(i + 1)
        images = []
        for j in range(2):
            image = pygame.image.load(path + "aliens/" + name + "/" + str(j) + ".png")
            image.set_colorkey((255,0,255))
            image = pygame.transform.scale(image, (image.get_width() * MULT, image.get_height() * MULT))
            images.append(image)

        sprites[name] = images

    sprites["player"] = [pygame.image.load(path + "player/" + n + ".png") for n in ["normal", "destroyed"]]

    return sprites

SPRITES = load_sprites()
