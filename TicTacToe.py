import pygame
import sys
import Engine

# Initialize the pygame
pygame.init()

# Size
width = 600
height = 400

# Create the screen
screen = pygame.display.set_mode([width, height])

# Color
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
cyan = (0, 225, 225)


# Font En-us
midFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 28)
largeFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 40)
moveFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 60)


class Button:
    def __init__(self, text, pos):
        self.btn = pygame.Rect(pos)
        self.text = midFont.render(text, True, cyan)
        self.rect = self.text.get_rect()
        self.rect.center = self.btn.center
        pygame.draw.rect(screen, grey, self.btn)
        self.draw()

    def draw(self):
        screen.blit(self.text, self.btn)


# Button
DarkBtn = Button('Dark Mode', [(width / 8), (height / 2), width / 4, 50])
LightBtn = Button('Light Mode', [5 * (width / 8), (height / 2), width / 4, 50])

# Title and Icon
pygame.display.set_caption('Tic-Tac-Toe')
icon = pygame.image.load('assets/icon/icon.png')
pygame.display.set_icon(icon)

# Game Starter
bcg = None
user = None
board = Engine.init_state()
turn = False

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # RGB - Red, Green, Blue
    screen.fill(grey)

    if bcg is None:
        DarkBtn = Button('Dark Mode', [(width / 8), (height / 2), width / 4, 50])
        LightBtn = Button('Light Mode', [5 * (width / 8), (height / 2), width / 4, 50])
        # screen.blit(DarkBtn.text, DarkBtn.btn)
        # screen.blit(LightBtn.text, LightBtn.btn)

    pygame.display.update()
    # if user is None:
    #
    #     title = largeFontFa.render('دوز', True, black)
    #     titleRect = title.get_rect()
    #     titleRect.center = ((width / 2), 50)
    #     screen.blit(title, titleRect)
    #     pygame.display.update()
    # titleReact =
