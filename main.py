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
highlight = pygame.image.load("assets/blue.png")

# Initialize a game board
board = Board(starting_positions)
# for s in board.squares:
#     if s:
#         print(s.board_index)

# Useful variables
selected_piece = None

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
            curr_square_index = get_index_from_click(click)

            # Is a piece selected?
            if selected_piece:
                # If click was on selected piece...
                if selected_piece.board_index == curr_square_index:
                    # Deselect the piece
                    selected_piece = None
                # If click was on possible move...
                elif selected_piece.clicked_possible_move(click):
                    # Make the move from old position to click
                    board.move_selected_piece(selected_piece.board_index, click)
                    selected_piece = None
                else:
                    selected_piece = None

            # If no piece is selected...
            elif selected_piece is None:
                # If click was made on a piece...
                if board.squares[curr_square_index]:
                    # Select the piece
                    selected_piece = board.squares[curr_square_index]
                    selected_piece.calculate_moves(board)
                # If click was on empty square, do nothing
                # This can be deleted later. Here for the sake of clarity
                else:
                    pass

    # Erase previous screen
    screen.fill('#ffffff')

    # Draw the board
    screen.blit(board.img, (0, 0))

    # Draw pieces and then highlight possible moves if a piece is selected
    for s in board.squares:
        if s:
            screen.blit(s.img, (get_blit_tuple_from_index(s.board_index, height)))
    if selected_piece:
        screen.blit(highlight, (get_blit_tuple_from_index(selected_piece.board_index, height)))

    # Display the board
    pygame.display.flip()
