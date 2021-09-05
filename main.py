import copy
import sys
import pygame
from board import Board
from data import starting_positions, checkmate_position, castling_position
from custom_functions import *
from piece import Piece

# TODO: Display material counts on the side
# TODO: Navigation buttons to restart, pause, go home, etc


# ------------- BUTTON CLASS ------------- #
# ######################################## #
class Button:
    def __init__(self, rect, command):
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(self.color)
        self.command = command

    def render(self, screen_):
        screen_.blit(self.image, self.rect)

    def get_event(self, event_):
        if event_.type == pygame.MOUSEBUTTONDOWN and event_.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.command()


# ------------- INITIALIZATION ------------- #
# ########################################## #

# Initialize pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('Chess')

# Create pygame screen
size = width, height = 1100, 800
screen = pygame.display.set_mode(size)
hl_size = 50  # Size of the highlights in px when a piece is selected

# Load images
home_title = pygame.image.load("assets/home-title-img.png")
play_btn_img = pygame.image.load("assets/play-img.png")
highlight_blue = pygame.image.load("assets/blue.png")
highlight_blue.fill((255, 255, 255, 80), None, pygame.BLEND_RGBA_MULT)
highlight_blue = pygame.transform.scale(highlight_blue, (hl_size, hl_size))
welcome_img = pygame.image.load("assets/welcome-img.png")
w_wins_checkmate_img = pygame.image.load("assets/w_wins_checkmate.png")
w_wins_timeout_img = pygame.image.load("assets/w_wins_timeout.png")
b_wins_checkmate_img = pygame.image.load("assets/b_wins_checkmate.png")
b_wins_timeout_img = pygame.image.load("assets/b_wins_timeout.png")
check_notify_img = pygame.image.load("assets/check_notify_img.png")

# Init fonts
font = pygame.font.SysFont('Comic Sans MS', 30)
timer_color = pygame.Color("#ffffff")
warning_color = pygame.Color("#ff0000")


# Screen navigation toggle method
def toggle_screen():
    global current_screen
    current_screen = "HOME" if curr_player == "GAME" else "GAME"


# Create buttons
play_home_btn = Button((400, 500, 300, 150), toggle_screen)

# Initialize a game board
board = Board(starting_positions)

# Useful variables
selected_piece = None
curr_player = "w"
check_notify = False
game_over = False
move_history = []
current_screen = "GAME"
win_type = ""  # Can be mate or clock currently

# ------------- GAME LOOP ------------- #
# ##################################### #

# Begin the clock
start_ticks = pygame.time.get_ticks()
white_seconds = 15
black_seconds = 15
white_clock_color = timer_color
black_clock_color = timer_color
now_time = 0

# Begin the game
while 1:
    if not game_over:
        # Check player clocks
        if white_seconds <= 0 or black_seconds <= 0:
            game_over = True
            win_type = "clock"
        if white_seconds <= 10:
            white_clock_color = warning_color
        if black_seconds <= 10:
            black_clock_color = warning_color

        # Make clock adjustments
        last_time = now_time
        now_time = (pygame.time.get_ticks() - start_ticks) / 1000
        elapsed_time = now_time - last_time
        if curr_player == "w":
            white_seconds -= elapsed_time
        if curr_player == "b":
            black_seconds -= elapsed_time

    # Handle all clicks and events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if current_screen == "GAME":
            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Get the position of the click
                click = pygame.mouse.get_pos()
                # Get square index of click
                curr_square_index = get_index_from_click(click)

                # Is a piece selected?
                if selected_piece:
                    # If click was on selected piece...
                    if selected_piece.board_index == curr_square_index:
                        # Deselect the piece
                        selected_piece = None
                    # If click was on possible move...
                    elif selected_piece.clicked_possible_move(click):
                        # Make sure the king is not in check
                        proposed_move_index = get_index_from_click(click)
                        future_board = Board(copy.copy(board.squares))
                        future_board.squares[proposed_move_index] = copy.copy(selected_piece)
                        future_board.squares[proposed_move_index].board_index = proposed_move_index
                        future_board.squares[selected_piece.board_index] = None
                        if king_is_in_check(future_board, selected_piece.color):
                            selected_piece = None
                        # Make the move
                        else:
                            # Remove the check GUI notification
                            check_notify = False

                            # This is used for en passant checking
                            old_pos = get_row_col_from_index(selected_piece.board_index)
                            moved_to = board.squares[get_index_from_click(click)]
                            new_pos = get_row_col_from_click(click)

                            # Make the move from old position to click
                            board.move_piece(selected_piece.board_index, get_row_col_from_click(click))

                            # Castling special cases
                            if not selected_piece.moved and get_row_col_from_click(click) in [(1, 3), (1, 7), (8, 3), (8, 7)] \
                                    and selected_piece.piece_type == "k":
                                if get_row_col_from_click(click) == (1, 3):
                                    board.move_piece(board.squares[0].board_index, (1, 4))
                                elif get_row_col_from_click(click) == (1, 7):
                                    board.move_piece(board.squares[7].board_index, (1, 6))
                                elif get_row_col_from_click(click) == (8, 3):
                                    board.move_piece(board.squares[56].board_index, (8, 4))
                                elif get_row_col_from_click(click) == (8, 7):
                                    board.move_piece(board.squares[63].board_index, (8, 6))

                            # En Passant special cases
                            if selected_piece.piece_type == "p" and moved_to is None and old_pos[1] != new_pos[1]:
                                if selected_piece.color == "w":
                                    board.kill_piece(get_index_from_row_col((new_pos[0] - 1, new_pos[1])))
                                if selected_piece.color == "b":
                                    board.kill_piece(get_index_from_row_col((new_pos[0] + 1, new_pos[1])))

                            # Promotion special cases
                            if selected_piece.piece_type == "p":
                                if selected_piece.color == "w" and new_pos[0] == 8:
                                    i = get_index_from_row_col(new_pos)
                                    board.squares[i] = Piece("assets/wq.png", 8, new_pos[1], "q", "w")
                                if selected_piece.color == "b" and new_pos[0] == 1:
                                    i = get_index_from_row_col(new_pos)
                                    board.squares[i] = Piece("assets/bq.png", 1, new_pos[1], "q", "b")

                            # Track move history
                            move_history.append({"piece_type": selected_piece.piece_type,
                                                 "color": selected_piece.color,
                                                 "from": old_pos,
                                                 "to": get_row_col_from_index(selected_piece.board_index)})

                            # Update moved attribute
                            selected_piece.moved = True
                            # Deselect current piece
                            selected_piece = None
                            # Switch active player
                            curr_player = "w" if curr_player == "b" else "b"

                            # Check for mate
                            if board.checkmate(curr_player):
                                game_over = True
                                win_type = "mate"
                            # Check for check
                            if king_is_in_check(board, curr_player) and not game_over:
                                check_notify = True
                    else:
                        selected_piece = None

                # If no piece is selected...
                elif selected_piece is None:
                    # If click was made on a piece...
                    if board.squares[curr_square_index] and board.squares[curr_square_index].color == curr_player:
                        # Select the piece
                        selected_piece = board.squares[curr_square_index]
                        # Calculate possible moves
                        selected_piece.calculate_moves(board)
                        # Add extra moves for castling
                        if selected_piece.piece_type == "k" and not selected_piece.moved:
                            selected_piece.possible_moves.extend(castling_moves_allowed(board, selected_piece.color))
                        # Add En Passant moves
                        if selected_piece.piece_type == "p":
                            row = get_row_col_from_index(selected_piece.board_index)[0]
                            if selected_piece.color == "w":
                                if row == 5 and move_history[-1]["piece_type"] == "p" and move_history[-1]["from"][0] == 7 \
                                        and move_history[-1]["to"][0] == 5:
                                    selected_piece.possible_moves.append((row + 1, move_history[-1]["to"][1]))
                            if selected_piece.color == "b":
                                if row == 4 and move_history[-1]["piece_type"] == "p" and move_history[-1]["from"][0] == 2 \
                                        and move_history[-1]["to"][0] == 4:
                                    selected_piece.possible_moves.append((row - 1, move_history[-1]["to"][1]))

        if current_screen == "HOME":
            play_home_btn.get_event(event)

    # ------------- DISPLAY SECTION ------------- #
    # ########################################### #
    if current_screen == "GAME":
        # Erase previous screen
        screen.fill('#ffffff')

        # Draw the board
        screen.blit(board.img, (0, 0))

        # Draw sidebar
        pygame.draw.rect(screen, pygame.Color("#334257"), pygame.Rect(800, 0, width - 800, height))
        screen.blit(welcome_img, (830, 30))
        screen.blit(font.render(str(round(white_seconds, 1)), True, white_clock_color), (900, 300))
        pygame.draw.circle(screen, pygame.Color("#ffffff"), (850, 323), 15, 0)
        screen.blit(font.render(str(round(black_seconds, 1)), True, black_clock_color), (900, 400))
        pygame.draw.circle(screen, pygame.Color("#000000"), (850, 423), 15, 0)

        # Draw pieces and then highlight possible moves if a piece is selected
        for s in board.squares:
            if s:
                if s is not selected_piece:
                    screen.blit(s.img, (get_blit_tuple_from_index(s.board_index, height)))
                else:
                    init_pos = get_blit_tuple_from_index(s.board_index, height)
                    screen.blit(pygame.transform.scale(s.img, (110, 110)), (init_pos[0] - 5, init_pos[1] - 7))
                    for move in selected_piece.possible_moves:
                        init_pos = get_blit_tuple_from_row_col(move, height)
                        screen.blit(highlight_blue, (init_pos[0] + hl_size / 2, init_pos[1] + hl_size / 2))

        if check_notify:
            screen.blit(check_notify_img, (830, 400))

        if game_over:
            if curr_player == "b":
                if win_type == "mate":
                    screen.blit(w_wins_checkmate_img, (170, 270))
                elif win_type == "clock":
                    screen.blit(w_wins_timeout_img, (170, 270))
            else:
                if win_type == "mate":
                    screen.blit(b_wins_checkmate_img, (170, 270))
                elif win_type == "clock":
                    screen.blit(b_wins_timeout_img, (170, 270))

    elif current_screen == "HOME":
        screen.fill("#334257")
        screen.blit(home_title, (150, 100))
        play_home_btn.render(screen)
        screen.blit(play_btn_img, (400, 500))

    # Display the board
    pygame.display.flip()
