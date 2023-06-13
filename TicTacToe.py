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
cyan = (0, 225, 225)
dark_Blue = (0, 0, 153)
dark_pink = (255, 0, 127)
color_finish = red
color_Screen = (128, 128, 128)
color_Game = black
color_board_line = green
color_Move = green
color_Computer = dark_pink

# Create the screen
screen = pygame.display.set_mode([width, height])

# Title and Icon
pygame.display.set_caption('Tic-Tac-Toe')
icon = pygame.image.load('assets/icon/icon.png')
pygame.display.set_icon(icon)

# Font En-us
midFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 28)
largeFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 40)
moveFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 60)

# Position
posBtn1 = [25, height - 60, width / 4, 50]
posBtn2 = [400, height - 60, width / 3.5, 50]
posBtn3 = [(width / 8), (height / 2), width / 3.7, 50]
posBtn4 = [5 * (width / 8), (height / 2), width / 3.7, 50]
posBtn5 = [(width / 2.8), (height - 65), width / 3, 50]
# -------------------------------------------------------
posTit1 = [(width / 2), 50]
posTit2 = [(width / 2), 30]
posTit3 = [width / 2 - (1.5 * 80), height / 2 - (1.5 * 80)]

# Draw Board
title_size = 80
title_origin = posTit3


# Title Class
class Title:
    def __init__(self, text, pos, color):
        self.text = largeFont.render(text, True, color)
        self.title = self.text.get_rect()
        self.title.center = pos
        screen.blit(self.text, self.title)


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


class ButtonTit:
    def __init__(self, text, pos):
        self.btn = pygame.Rect(pos)
        self.text = midFont.render(text, True, color_Game)
        self.rect = self.text.get_rect()
        self.rect.center = self.btn.center
        self.draw()

    def draw(self):
        screen.blit(self.text, self.btn)

    def Btn(self):
        return self.btn


# Game Starter Parameter
bcg = None
User = None
board = Engine.init_state()
turn = False
main_menu = False


# Draw Screen
def draw_screen(color):
    screen.fill(color)


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # BackGround Color

    screen.fill(color_Screen)

    if bcg is None:
        DarkBtn = Button('Dark Mode', posBtn1)
        LightBtn = Button('Light Mode', posBtn2)
        color_Game = cyan
        title_welcome = Title('Welcome', posTit1, color_Game)

        if DarkBtn.check_click() == 1:
            color_Screen = black
            color_Game = green
            # color_board_line = green
            # color_Move = green
            time.sleep(0.2)
            bcg = True

        elif LightBtn.check_click() == 1:
            color_Screen = white
            color_Game = dark_Blue
            color_board_line = dark_Blue
            color_Move = dark_Blue
            time.sleep(0.2)
            bcg = True

    else:
        # Game Env
        if User is None:

            # Draw title
            title = Title("Play Tic-Tac-Toe", posTit1, color_Game)

            # Draw buttons
            PlayXBtn = ButtonTit("Play as X", posBtn3)
            PlayOBtn = ButtonTit("Play as O", posBtn4)

            # Check if button is clicked
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if PlayXBtn.Btn().collidepoint(mouse):
                    time.sleep(0.2)
                    User = Engine.X
                elif PlayOBtn.Btn().collidepoint(mouse):
                    time.sleep(0.2)
                    User = Engine.O

        else:

            # Draw game board
            titles = []
            for i in range(3):
                row = []
                for j in range(3):
                    rect = pygame.Rect(
                        title_origin[0] + j * title_size,
                        title_origin[1] + i * title_size,
                        title_size, title_size
                    )
                    pygame.draw.rect(screen, color_board_line, rect, 3)

                    if board[i][j] != Engine.EMPTY:
                        move = moveFont.render(board[i][j], True, color_Move)
                        moveRect = move.get_rect()
                        moveRect.center = rect.center
                        screen.blit(move, moveRect)
                    row.append(rect)
                titles.append(row)

            game_over = Engine.terminal(board)
            player = Engine.player(board)

            # Show title
            if game_over:
                winner = Engine.winner(board)
                if winner is None:
                    title_finish = Title(f"Game End: Tie.", posTit2, color_finish)
                else:
                    title_finish = Title(f"Game Over: {winner} wins.", posTit2, color_finish)
            elif User == player:
                title = Title(f"Play as {User}", posTit2, color_Game)
            else:
                title = Title(f"Computer thinking...", posTit2, color_Computer)

            # Check for AI move
            if User != player and not game_over:
                if turn:
                    time.sleep(0.5)
                    move = Engine.minimax(board)
                    board = Engine.result(board, move)
                    turn = False
                else:
                    turn = True

            # Check for a User move
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1 and User == player and not game_over:
                mouse = pygame.mouse.get_pos()
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == Engine.EMPTY and titles[i][j].collidepoint(mouse):
                            board = Engine.result(board, (i, j))

            if game_over:
                PlayAgainBtn = ButtonTit("Play Again", posBtn5)
                click, _, _ = pygame.mouse.get_pressed()
                if click == 1:
                    mouse = pygame.mouse.get_pos()
                    if PlayAgainBtn.btn.collidepoint(mouse):
                        time.sleep(0.2)
                        User = None
                        board = Engine.init_state()
                        turn = False

    pygame.display.flip()
