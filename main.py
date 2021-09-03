import copy
import sys
import pygame
from board import Board
from data import starting_positions
from custom_functions import *

# Initialize pygame
pygame.init()

# Create pygame screen
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
highlight_blue = pygame.image.load("assets/blue.png")
highlight_red = pygame.image.load("assets/red.png")

# Initialize a game board
board = Board(starting_positions)
# for s in board.squares:
#     if s:
#         print(s.board_index)

# Useful variables
selected_piece = None
curr_player = "w"
in_check = False

# Begin the game
while 1:
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            sys.exit()

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
                    in_check = king_is_in_check(future_board, selected_piece.color)
                    del future_board
                    if in_check:
                        print("Move not allowed. King in check.")
                        selected_piece = None
                    # Make the move
                    else:
                        # Make the move from old position to click
                        board.move_selected_piece(selected_piece.board_index, click)
                        # Deselect current piece
                        selected_piece = None
                        # See if opposing king is in check
                        # in_check = king_is_in_check(board, curr_player)
                        # Switch active player
                        curr_player = "w" if curr_player == "b" else "b"
                else:
                    selected_piece = None

            # If no piece is selected...
            elif selected_piece is None:
                # If click was made on a piece...
                if board.squares[curr_square_index] and board.squares[curr_square_index].color == curr_player:
                    # Select the piece
                    selected_piece = board.squares[curr_square_index]
                    selected_piece.calculate_moves(board)

    # Erase previous screen
    screen.fill('#ffffff')

    # Draw the board
    screen.blit(board.img, (0, 0))

    # Draw pieces and then highlight possible moves if a piece is selected
    for s in board.squares:
        if s:
            screen.blit(s.img, (get_blit_tuple_from_index(s.board_index, height)))
    if selected_piece:
        screen.blit(highlight_blue, (get_blit_tuple_from_index(selected_piece.board_index, height)))
        for move in selected_piece.possible_moves:
            screen.blit(highlight_red, (get_blit_tuple_from_row_col(move, height)))

    # Display the board
    pygame.display.flip()
