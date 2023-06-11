import pygame
import sys
import Engine

# Initialize the pygame
pygame.init()

# Color
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Font Fa-ir
midFontFa = pygame.font.Font('assets/font/Sahel-Light.ttf', 28)
largeFontFa = pygame.font.Font('assets/font/Sahel-Light.ttf', 40)
moveFontFa = pygame.font.Font('assets/font/Sahel-Light.ttf', 60)

# Font En-us
midFontEn = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 28)
largeFontEn = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 40)
moveFontEn = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 60)


# Create the screen
screen = pygame.display.set_mode((400, 600))

# Title and Icon
pygame.display.set_caption('Tic-Tac-Toe')
icon = pygame.image.load('assets/icon/icon.png')
pygame.display.set_icon(icon)

# Game Starter
user = None
board = Engine.init_state()
turn = False


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # RGB - Red, Green, Blue
    screen.fill(white)
    pygame.display.update()

    if user is None:
        pass
        # title =
        # titleReact =