import pygame
from custom_functions import get_position_from_click


class Board:
    """Class that represents the current status of each square on the board"""
    def __init__(self, position_list):
        self.img = pygame.image.load("assets/board.png")
        self.squares = position_list

    def set_board(self, positions: list):
        """Pass in a 2d list of positions and the board squares will update"""
        self.squares = []
        for p in positions:
            self.squares.append(p)

    def get_clicked_piece(self, click: tuple):
        """Returns piece that was clicked or None if square is empty"""
        r_click, c_click = get_position_from_click(click)

        for r in range(len(self.squares)):
            for c in range(len(self.squares[r])):
                s = self.squares[r][c]
                if s:
                    if s.row == r_click and s.col == c_click:
                        return s
        return None

    def deselect_all(self):
        """Deselects all of the squares"""
        for r in range(len(self.squares)):
            for c in range(len(self.squares[r])):
                s = self.squares[r][c]
                if s:
                    s.selected = False

    def clicked_possible_move(self, click: tuple):
        """Returns true if a click was made on a possible move of the selected piece"""
        r_click, c_click = get_position_from_click(click)

        for r in range(len(self.squares)):
            for c in range(len(self.squares[r])):
                s = self.squares[r][c]
                if s and s.selected:
                    for move in s.possible_moves:
                        if move[0] == r_click and move[1] == c_click:
                            return True

    def move_selected_piece(self, click):
        r_click, c_click = get_position_from_click(click)

        for r in range(len(self.squares)):
            for c in range(len(self.squares[r])):
                s = self.squares[r][c]
                if s:
                    if s.selected:
                        s.row = r_click
                        s.col = c_click
                        s.selected = False
                        s.possible_moves = []
