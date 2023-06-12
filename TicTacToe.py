import pygame
import sys
import Engine

# Initialize the pygame
pygame.init()

# Size
width = 600
height = 400

# Color
# RGB - Red, Green, Blue
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
cyan = (0, 225, 225)

# Create the screen
screen = pygame.display.set_mode([width, height])
screen.fill(gray)

# Font En-us
midFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 28)
largeFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 40)
moveFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 60)


# Button Class

class Button:
    def __init__(self, text, pos):
        self.pos = pos
        self.btn = pygame.Rect(pos)
        self.text = midFont.render(text, True, cyan)
        self.rect = self.text.get_rect()
        self.rect.center = self.btn.center
        pygame.draw.rect(screen, 'dark gray', self.btn)
        self.draw()

    def draw(self):
        screen.blit(self.text, self.btn)
        if self.check_click():
            pygame.draw.rect(screen, 'light gray', self.btn)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect(self.pos)
        if left_click and button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False


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

    if bcg is None:
        DarkBtn = Button('Dark Mode', [(width / 8), (height / 2), width / 4, 50])
        LightBtn = Button('Light Mode', [5 * (width / 8), (height / 2), width / 3.5, 50])
        if DarkBtn.check_click():
            screen.fill(black)
        elif LightBtn.check_click():
            screen.fill(white)

    pygame.display.update()
