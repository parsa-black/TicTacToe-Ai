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
pos1 = [25, 350, width / 4, 50]
pos2 = [400, 350, width / 3.5, 50]
pos3 = [(width / 8), (height / 2), width / 4, 50]
pos4 = [5 * (width / 8), (height / 2), width / 4, 50]
pos5 = [width / 3, height - 65, width / 3, 50]


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
            return 1
        else:
            return 0


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

    # BackGround Color
    if bcg is None:

        DarkBtn = Button('Dark Mode', pos1)
        LightBtn = Button('Light Mode', pos2)

        if DarkBtn.check_click() == 1:
            time.sleep(0.2)
            screen.fill(black)
        elif LightBtn.check_click() == 1:
            time.sleep(0.2)
            screen.fill(white)

    # Game Env
    if User is None:

        # Title
        title = largeFont.render("Tic-Tac-Toe Game", True, cyan)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Game Btn
        PlayXBtn = Button('Play as X', pos3)
        PlayOBtn = Button('Play as O', pos4)

        # Check
        if PlayXBtn.check_click() == 1:
            time.sleep(0.2)
            User = Engine.X
        elif PlayOBtn.check_click() == 1:
            time.sleep(0.2)
            User = Engine.O

    else:

        # Draw Board
        title_size = 80
        title_origin = (width / 2 - (1.5 * title_size),
                        height / 2 - (1.5 * title_size))
        titles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    title_origin[0] + j * title_size,
                    title_origin[1] + i * title_size,
                    title_size, title_size
                )
                pygame.draw.rect(screen, cyan, rect, 3)

                if board[i][j] != Engine.EMPTY:
                    move = moveFont.render(board[i][j], True, cyan)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            titles.append(row)

        game_over = Engine.terminal(board)
        player = Engine.player(board)

        if game_over:
            winner = Engine.winner(board)
            if winner is None:
                title = "Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif User == player:
            title = f"Play as {User}"
        else:
            title = "Computer thinking..."

        title = largeFont.render(title, True, cyan)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # AI Move
        if User != player and not game_over:
            if turn:
                time.sleep(0.5)
                move = Engine.minimax(board)
                board = Engine.result(board, move)
                turn = False
            else:
                turn = True

        # User Move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and User == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if board[i][j] == Engine.EMPTY and titles[i][j].collidepoint(mouse):
                        board = Engine.result(board, (i, j))

        if game_over:
            AgainBtn = Button('Play Again', pos5)
            if AgainBtn.check_click() == 1:
                time.sleep(0.2)
                user = None
                board = Engine.init_state()
                turn = False
    pygame.display.update()
