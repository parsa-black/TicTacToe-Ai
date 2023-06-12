import pygame
import sys
import Engine

# Initialize the pygame
pygame.init()

# Size
width = 600
height = 400

# Create the screen
screen = pygame.display.set_mode((width, height))

# Color
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)


# Font En-us
midFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 28)
largeFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 40)
moveFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 60)


class Button:
    def __init__(self, text):
        self.text = midFont.render(text, True, white)
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.blit(self.text, (0, 0))


# Title and Icon
pygame.display.set_caption('Tic-Tac-Toe')
icon = pygame.image.load('assets/icon/icon.png')
pygame.display.set_icon(icon)

# Game Starter
lang = None
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

    if lang is None:
        FarsiButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        Farsi = midFont.render('english', True, white)
        FarsiRect = Farsi.get_rect()
        FarsiRect.center = FarsiButton.center
        pygame.draw.rect(screen, black, FarsiButton)
        screen.blit(Farsi, FarsiRect)

    pygame.display.update()
    # if user is None:
    #
    #     title = largeFontFa.render('دوز', True, black)
    #     titleRect = title.get_rect()
    #     titleRect.center = ((width / 2), 50)
    #     screen.blit(title, titleRect)
    #     pygame.display.update()
    # titleReact =
