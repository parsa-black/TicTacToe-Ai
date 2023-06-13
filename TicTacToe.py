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
gray_Screen = (128, 128, 128)
cyan = (0, 225, 225)
dark_Blue = (0, 0, 153)
dark_Purple = (0, 0, 153)

# Create the screen
screen = pygame.display.set_mode([width, height])


# Font En-us
midFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 28)
largeFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 40)
moveFont = pygame.font.Font('assets/font/RobotoMono-VariableFont_wght.ttf', 60)

# Button pos
posBtn1 = [25, 350, width / 4, 50]
posBtn2 = [400, 350, width / 3.5, 50]
posBtn3 = [(width / 8), (height / 2), width / 3.7, 50]
posBtn4 = [5 * (width / 8), (height / 2), width / 3.7, 50]
posBtn5 = [width / 3, height - 65, width / 3, 50]
# -------------------------------------------------------
posTit1 = [(width / 2), 50]


# Title Class
class Title:
    def __init__(self, text, pos):
        self.text = largeFont.render(text, True, green)
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
        self.text = midFont.render(text, True, green)
        self.rect = self.text.get_rect()
        self.rect.center = self.btn.center
        self.draw()

    def draw(self):
        pygame.draw.rect(screen, black, self.btn)
        screen.blit(self.text, self.btn)

    def Btn(self):
        return self.btn


# Title and Icon
pygame.display.set_caption('Tic-Tac-Toe')
icon = pygame.image.load('assets/icon/icon.png')
pygame.display.set_icon(icon)

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

    screen.fill(gray_Screen)

    if bcg is None:
        DarkBtn = Button('Dark Mode', posBtn1)
        LightBtn = Button('Light Mode', posBtn2)

        if DarkBtn.check_click() == 1:
            gray_Screen = black
            time.sleep(0.2)
            bcg = True

        elif LightBtn.check_click() == 1:
            gray_Screen = white
            # cyan = dark_Blue
            # green = dark_Purple
            time.sleep(0.2)
            bcg = True

    else:
        # Game Env
        if User is None:
            #
            # # Draw title
            # title_start = Title("Play Tic-Tac-Toe", posTit1)
            #
            # # Draw buttons
            # PlayXBtn = ButtonTit("Play as X", posBtn3)
            # PlayOBtn = ButtonTit("Play as O", posBtn4)
            #
            # # Check if button is clicked
            # click, _, _ = pygame.mouse.get_pressed()
            # if click == 1:
            #     mouse = pygame.mouse.get_pos()
            #     if PlayXBtn.Btn().collidepoint(mouse):
            #         time.sleep(0.2)
            #         User = Engine.X
            #     elif PlayOBtn.Btn().collidepoint(mouse):
            #         time.sleep(0.2)
            #         User = Engine.O

        else:

            # Draw game board
            tile_size = 80
            tile_origin = (width / 2 - (1.5 * tile_size),
                           height / 2 - (1.5 * tile_size))
            tiles = []
            for i in range(3):
                row = []
                for j in range(3):
                    rect = pygame.Rect(
                        tile_origin[0] + j * tile_size,
                        tile_origin[1] + i * tile_size,
                        tile_size, tile_size
                    )
                    pygame.draw.rect(screen, white, rect, 3)

                    if board[i][j] != Engine.EMPTY:
                        move = moveFont.render(board[i][j], True, white)
                        moveRect = move.get_rect()
                        moveRect.center = rect.center
                        screen.blit(move, moveRect)
                    row.append(rect)
                tiles.append(row)

            game_over = Engine.terminal(board)
            player = Engine.player(board)

            # Show title
            if game_over:
                winner = Engine.winner(board)
                if winner is None:
                    title = f"Game Over: Tie."
                else:
                    title = f"Game Over: {winner} wins."
            elif User == player:
                title = f"Play as {User}"
            else:
                title = f"Computer thinking..."
            title = largeFont.render(title, True, white)
            titleRect = title.get_rect()
            titleRect.center = ((width / 2), 30)
            screen.blit(title, titleRect)

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
                        if board[i][j] == Engine.EMPTY and tiles[i][j].collidepoint(mouse):
                            board = Engine.result(board, (i, j))

            if game_over:
                againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
                again = midFont.render("Play Again", True, black)
                againRect = again.get_rect()
                againRect.center = againButton.center
                pygame.draw.rect(screen, white, againButton)
                screen.blit(again, againRect)
                click, _, _ = pygame.mouse.get_pressed()
                if click == 1:
                    mouse = pygame.mouse.get_pos()
                    if againButton.collidepoint(mouse):
                        time.sleep(0.2)
                        User = None
                        board = Engine.init_state()
                        turn = False

    pygame.display.flip()
