import pygame
import sys

# Initialize the pygame
pygame.init()

# Color
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((400, 600))

# Title and Icon
pygame.display.set_caption('TicTacToe')
icon = pygame.image.load('assets/icon/icon.png')
pygame.display.set_icon(icon)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # RGB - Red, Green, Blue
    screen.fill(white)
    pygame.display.update()
