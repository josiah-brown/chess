import pygame


class Piece:
    """Class that represents a generic chess piece"""
    def __init__(self, img_path, row, col, piece_type, color):
        self.def_img = pygame.image.load(img_path)
        self.curr_img = pygame.image.load(img_path)
        self.rect = self.curr_img.get_rect()
        self.row = row
        self.col = col
        self.selected = False
        self.piece_type = piece_type
        self.color = color
        self.possible_moves = []

    def update_piece_img(self):
        """Updates the image of a piece to selected if piece is selected"""
        if self.selected:
            self.curr_img = pygame.image.load("assets/red.png")
        else:
            self.curr_img = self.def_img

    def check_if_square_empty(self, board, pos):
        """Returns true if the input position is empty on the board"""
        for r in range(len(board.squares)):
            for c in range(len(board.squares[r])):
                s = board.squares[r][c]
                if s:
                    if s.row == pos[0] and s.col == pos[1]:
                        return False
        return True

    def calculate_moves(self, b):
        available_moves = []
        if self.piece_type == "p":
            if self.color == "w":
                if self.row == 2:
                    if self.check_if_square_empty(b, (3, self.col)):
                        available_moves.append((3, self.col))
                        if self.check_if_square_empty(b, (4, self.col)):
                            available_moves.append((4, self.col))
                elif self.row < 8:
                    if self.check_if_square_empty(b, (self.row + 1, self.col)):
                        available_moves.append((self.row + 1, self.col))
            if self.color == "b":
                if self.row == 7:
                    if self.check_if_square_empty(b, (6, self.col)):
                        available_moves.append((6, self.col))
                        if self.check_if_square_empty(b, (5, self.col)):
                            available_moves.append((5, self.col))
                elif self.row > 1:
                    if self.check_if_square_empty(b, (self.row - 1, self.col)):
                        available_moves.append((self.row - 1, self.col))

        if self.piece_type == "b":
            for i, c in enumerate(range(self.col, 8)):
                if self.check_if_square_empty(b, (self.row + i + 1, c + 1)):
                    available_moves.append((self.row + i + 1, c + 1))
                else:
                    break
            for i, c in enumerate(range(self.col, 8)):
                if self.check_if_square_empty(b, (self.row - (i + 1), c + 1)):
                    available_moves.append((self.row - (i + 1), c + 1))
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, self.col)))):
                if self.check_if_square_empty(b, (self.row - (self.col - (i + 1)), c)):
                    available_moves.append((self.row - (self.col - (i + 1)), c))
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, self.col)))):
                if self.check_if_square_empty(b, (self.row + (self.col - (i + 1)), c)):
                    available_moves.append((self.row + (self.col - (i + 1)), c))
                else:
                    break

        if self.piece_type == "r":
            for i in range(self.col+1, 9):
                if self.check_if_square_empty(b, (self.row, i)):
                    available_moves.append((self.row, i))
                else:
                    break
            for i in reversed(range(1, self.col)):
                if self.check_if_square_empty(b, (self.row, i)):
                    available_moves.append((self.row, i))
                else:
                    break
            for i in range(self.row+1, 9):
                if self.check_if_square_empty(b, (i, self.col)):
                    available_moves.append((i, self.col))
                else:
                    break
            for i in reversed(range(1, self.row)):
                if self.check_if_square_empty(b, (i, self.col)):
                    available_moves.append((i, self.col))
                else:
                    break

        if self.piece_type == "q":
            for i, c in enumerate(range(self.col, 8)):
                if self.check_if_square_empty(b, (self.row + i + 1, c + 1)):
                    available_moves.append((self.row + i + 1, c + 1))
                else:
                    break
            for i, c in enumerate(range(self.col, 8)):
                if self.check_if_square_empty(b, (self.row - (i + 1), c + 1)):
                    available_moves.append((self.row - (i + 1), c + 1))
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, self.col)))):
                if self.check_if_square_empty(b, (self.row - (self.col - (i + 1)), c)):
                    available_moves.append((self.row - (self.col - (i + 1)), c))
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, self.col)))):
                if self.check_if_square_empty(b, (self.row + (self.col - (i + 1)), c)):
                    available_moves.append((self.row + (self.col - (i + 1)), c))
                else:
                    break
            for i in range(self.col + 1, 9):
                if self.check_if_square_empty(b, (self.row, i)):
                    available_moves.append((self.row, i))
                else:
                    break
            for i in reversed(range(1, self.col)):
                if self.check_if_square_empty(b, (self.row, i)):
                    available_moves.append((self.row, i))
                else:
                    break
            for i in range(self.row + 1, 9):
                if self.check_if_square_empty(b, (i, self.col)):
                    available_moves.append((i, self.col))
                else:
                    break
            for i in reversed(range(1, self.row)):
                if self.check_if_square_empty(b, (i, self.col)):
                    available_moves.append((i, self.col))
                else:
                    break

        if self.piece_type == "k":
            for y in range(self.row-1, self.row+2):
                for x in range(self.col-1, self.col+2):
                    if self.check_if_square_empty(b, (y, x)):
                        available_moves.append((y, x))

        if self.piece_type == "n":
            n_moves = [(self.row + 2, self.col - 1), (self.row + 2, self.col + 1),
                       (self.row + 1, self.col + 2), (self.row - 1, self.col + 2),
                       (self.row - 2, self.col + 1), (self.row - 2, self.col - 1),
                       (self.row - 1, self.col - 2), (self.row + 1, self.col - 2)]
            for move in n_moves:
                if self.check_if_square_empty(b, move):
                    available_moves.append(move)

        # Remove all moves that fall off the board
        for i, move in reversed(list(enumerate(available_moves))):
            if move[0] < 1 or move[0] > 8 or move[1] > 8 or move[1] < 1:
                available_moves.pop(i)

        # Remove all moves that land on another piece
        for r in range(len(b.squares)):
            for c in range(len(b.squares[r])):
                s = b.squares[r][c]
                if s:
                    if (s.row, s.col) in available_moves:
                        available_moves.remove((s.row, s.col))

        self.possible_moves = available_moves
