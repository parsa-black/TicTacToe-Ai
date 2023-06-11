import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((600, 800))

# Title and Icon
pygame.display.set_caption('TicTacToe')
icon = pygame.image.load('assets/icon/icon.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB - Red, Green, Blue
    screen.fill((255, 150, 15))
    pygame.display.update()
