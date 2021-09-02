import pygame
from custom_functions import *


class Board:
    """Class that represents the current status of each square on the board"""
    def __init__(self, position_list):
        self.img = pygame.image.load("assets/board.png")
        self.squares = position_list

    def set_board(self, positions: list):
        """Pass in a 2d list of positions and the board squares will update (useful later for setting up end games)"""
        self.squares = []
        for p in positions:
            self.squares.append(p)

    def get_clicked_piece(self, click: tuple):
        """Returns piece that was clicked or None if square is empty"""
        r_click, c_click = get_row_col_from_click(click)

        for s in self.squares:
            if s:
                if s.row == r_click and s.col == c_click:
                    return s
        return None

    def deselect_all(self):
        """Deselects all of the squares"""
        for s in self.squares:
            if s:
                s.selected = False

    def move_selected_piece(self, old_pos_index, new_pos):
        """Moves the selected piece to clicked square, clears possible moves, and deselects"""
        r_new, c_new = get_row_col_from_click(new_pos)
        new_index = get_index_from_row_col((r_new, c_new))

        # Remove opposing piece if attack was made
        if self.squares[new_index]:
            self.squares[new_index] = None
        # New square contains the piece
        self.squares[new_index] = self.squares[old_pos_index]
        # Update piece index
        self.squares[new_index].board_index = new_index
        # Clear possible moves
        self.squares[new_index].possible_moves = []
        # Remove piece from old square
        self.squares[old_pos_index] = None
