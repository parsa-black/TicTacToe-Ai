import pygame
import sys
import time
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

# Button pos
pos1 = [(width / 8), (height / 2), width / 4, 50]
pos2 = [5 * (width / 8), (height / 2), width / 4, 50]
pos3 = [5 * (width / 8), (height / 2), width / 3.5, 50]


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


# Game Starter Parameter
bcg = None
User = None
board = Engine.init_state()
turn = False


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Game Env
    def draw_game():
        
        if User is None:

            # Title
            title = largeFont.render("Tic-Tac-Toe Game", True, cyan)
            titleRect = title.get_rect()
            titleRect.center = ((width / 2), 50)
            screen.blit(title, titleRect)

            # Game Btn
            PlayXBtn = Button('Play as X', pos1)
            PlayOBtn = Button('Play as O', pos2)
            if PlayXBtn:
                time.sleep(0.2)
                User = Engine.X
            elif PlayOBtn:
                time.sleep(0.2)
                User = Engine.O
        else:
            pass


    if bcg is None:
        DarkBtn = Button('Dark Mode', pos1)
        LightBtn = Button('Light Mode', pos3)
        if DarkBtn.check_click():
            time.sleep(0.1)
            screen.fill(black)
            time.sleep(0.3)
            draw_game()
        elif LightBtn.check_click():
            time.sleep(0.1)
            screen.fill(white)
            time.sleep(0.3)
            draw_game()

    pygame.display.flip()
