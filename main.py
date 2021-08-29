import sys
import pygame
from piece import Piece
from board import Board
from data import starting_positions

# Initialize pygame
pygame.init()

# Create pygame screen
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
highlight = pygame.image.load("assets/blue.png")

# Initialize a game board
board = Board(starting_positions)

# Begin the game
while 1:
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            sys.exit()

        # Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Get the position of the click
            pos = pygame.mouse.get_pos()

            # Store the clicked piece
            curr_piece = board.get_clicked_piece(pos)

            # If the piece exists
            if curr_piece:
                # If it was already selected, deselect
                if curr_piece.selected:
                    curr_piece.selected = False
                # Otherwise, select the piece
                else:
                    board.deselect_all()
                    curr_piece.selected = True

            if board.clicked_possible_move(pos):
                board.move_selected_piece(pos)

    # Erase previous screen
    screen.fill('#ffffff')

    # Draw all current elements onto screen
    screen.blit(board.img, (0, 0))
    for r in range(len(board.squares)):
        for c in range(len(board.squares[r])):
            s = board.squares[r][c]
            if s:
                s.update_piece_img()
                screen.blit(s.curr_img, ((s.col - 1) * 100, height - s.row * 100))
                if s.selected:
                    s.calculate_moves(board)
                    for m in s.possible_moves:
                        screen.blit(highlight, ((m[1] - 1) * 100, height - m[0] * 100))

    # Display the board
    pygame.display.flip()
