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


class Button:
    def __init__(self, text):
        self.text = midFontEn.render(text, True, white)
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.blit(self.text, (0, 0))


button1 = Button('Farsi')
button2 = Button('English')

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
    screen.blit(button1.surface, (170, 240))
    screen.blit(button2.surface, (150, 280))
    pygame.display.update()

    if user is None:
        pass
        # title =
        # titleReact =
