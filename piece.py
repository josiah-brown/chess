import pygame
from custom_functions import *


class Piece:
    """Class that represents a generic chess piece"""
    def __init__(self, img_path, row, col, piece_type, color):
        self.img = pygame.image.load(img_path)
        self.rect = self.img.get_rect()
        self.board_index = (col - 1) + (row - 1) * 8
        self.selected = False
        self.piece_type = piece_type
        self.color = color
        self.possible_moves = []

    def calculate_moves(self, b):
        """Pass in the current board and set the pieces possible_moves attribute to a list of all possible moves"""
        available_moves = []
        row, col = get_row_col_from_index(self.board_index)

        if self.piece_type == "p":
            if self.color == "w":
                if row == 2:
                    if check_if_square_empty(b, (3, col)):
                        available_moves.append((3, col))
                        if check_if_square_empty(b, (4, col)):
                            available_moves.append((4, col))
                elif row < 8:
                    if check_if_square_empty(b, (row + 1, col)):
                        available_moves.append((row + 1, col))
            if self.color == "b":
                if row == 7:
                    if check_if_square_empty(b, (6, col)):
                        available_moves.append((6, col))
                        if check_if_square_empty(b, (5, col)):
                            available_moves.append((5, col))
                elif row > 1:
                    if check_if_square_empty(b, (row - 1, col)):
                        available_moves.append((row - 1, col))

        if self.piece_type == "b":
            for i, c in enumerate(range(col, 8)):
                if check_if_square_empty(b, (row + i + 1, c + 1)):
                    available_moves.append((row + i + 1, c + 1))
                else:
                    break
            for i, c in enumerate(range(col, 8)):
                if check_if_square_empty(b, (row - (i + 1), c + 1)):
                    available_moves.append((row - (i + 1), c + 1))
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, col)))):
                if check_if_square_empty(b, (row - (col - (i + 1)), c)):
                    available_moves.append((row - (col - (i + 1)), c))
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, col)))):
                if check_if_square_empty(b, (row + (col - (i + 1)), c)):
                    available_moves.append((row + (col - (i + 1)), c))
                else:
                    break

        if self.piece_type == "r":
            for i in range(col+1, 9):
                if check_if_square_empty(b, (row, i)):
                    available_moves.append((row, i))
                else:
                    break
            for i in reversed(range(1, col)):
                if check_if_square_empty(b, (row, i)):
                    available_moves.append((row, i))
                else:
                    break
            for i in range(row+1, 9):
                if check_if_square_empty(b, (i, col)):
                    available_moves.append((i, col))
                else:
                    break
            for i in reversed(range(1, row)):
                if check_if_square_empty(b, (i, col)):
                    available_moves.append((i, col))
                else:
                    break

        if self.piece_type == "q":
            for i, c in enumerate(range(col, 8)):
                if check_if_square_empty(b, (row + i + 1, c + 1)):
                    available_moves.append((row + i + 1, c + 1))
                else:
                    break
            for i, c in enumerate(range(col, 8)):
                if check_if_square_empty(b, (row - (i + 1), c + 1)):
                    available_moves.append((row - (i + 1), c + 1))
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, col)))):
                if check_if_square_empty(b, (row - (col - (i + 1)), c)):
                    available_moves.append((row - (col - (i + 1)), c))
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, col)))):
                if check_if_square_empty(b, (row + (col - (i + 1)), c)):
                    available_moves.append((row + (col - (i + 1)), c))
                else:
                    break
            for i in range(col + 1, 9):
                if check_if_square_empty(b, (row, i)):
                    available_moves.append((row, i))
                else:
                    break
            for i in reversed(range(1, col)):
                if check_if_square_empty(b, (row, i)):
                    available_moves.append((row, i))
                else:
                    break
            for i in range(row + 1, 9):
                if check_if_square_empty(b, (i, col)):
                    available_moves.append((i, col))
                else:
                    break
            for i in reversed(range(1, row)):
                if check_if_square_empty(b, (i, col)):
                    available_moves.append((i, col))
                else:
                    break

        if self.piece_type == "k":
            for y in range(row-1, row+2):
                for x in range(col-1, col+2):
                    if check_if_square_empty(b, (y, x)):
                        available_moves.append((y, x))

# TODO: Fix the board so that pieces are stored in the board squares where they actually appear on the screen.
#       Currently, each piece stores its own position and for some reason I am unable to delete pieces when they
#       have been attacked. I need to refactor all of the code and think about this before continuing

        if self.piece_type == "n":
            n_moves = [(row + 2, col - 1), (row + 2, col + 1),
                       (row + 1, col + 2), (row - 1, col + 2),
                       (row - 2, col + 1), (row - 2, col - 1),
                       (row - 1, col - 2), (row + 1, col - 2)]
            for move in n_moves:
                if check_if_square_empty(b, move):
                    available_moves.append(move)

        # Remove all moves that fall off the board
        for i, move in reversed(list(enumerate(available_moves))):
            if move[0] < 1 or move[0] > 8 or move[1] > 8 or move[1] < 1:
                available_moves.pop(i)

        # Remove all moves that land on another piece of same color
        for s in b.squares:
            if s:
                pos = get_row_col_from_index(s.board_index)
                if pos in available_moves:
                    if s.color == self.color:
                        available_moves.remove((s.row, s.col))

        self.possible_moves = available_moves

    def clicked_possible_move(self, click: tuple):
        """Returns true if a click was made on a possible move of the selected piece"""
        pos = get_row_col_from_click(click)

        for move in self.possible_moves:
            if pos == move:
                return True
        return False
