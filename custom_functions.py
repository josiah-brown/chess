

def get_row_col_from_click(click) -> tuple:
    """Pass in tuple that represents click coordinates and return (col, row) of click"""
    r, c = 0, 0

    if click[0] < 100:
        c = 1
    elif click[0] < 200:
        c = 2
    elif click[0] < 300:
        c = 3
    elif click[0] < 400:
        c = 4
    elif click[0] < 500:
        c = 5
    elif click[0] < 600:
        c = 6
    elif click[0] < 700:
        c = 7
    elif click[0] < 800:
        c = 8

    if click[1] < 100:
        r = 8
    elif click[1] < 200:
        r = 7
    elif click[1] < 300:
        r = 6
    elif click[1] < 400:
        r = 5
    elif click[1] < 500:
        r = 4
    elif click[1] < 600:
        r = 3
    elif click[1] < 700:
        r = 2
    elif click[1] < 800:
        r = 1
    return r, c


def square_is_empty(board, pos):
    """Returns true if the input position is empty on the board"""
    index = get_index_from_row_col(pos)
    if index < 64:
        if board.squares[index]:
            return False
    return True


def is_enemy(board, pos, color):
    """Returns true if square is enemy piece"""
    index = get_index_from_row_col(pos)
    if board.squares[index]:
        if board.squares[index].color != color:
            return True
    return False


def square_contains_enemy(board, pos, color):
    """Returns true if the input position contains an enemy"""
    for s in board.squares:
        if s:
            if s.row == pos[0] and s.col == pos[1] and (s.color != color):
                return True
    return False


def get_index_from_click(click):
    """Given a click tuple, returns the index of the click in the squares list"""
    r_click, c_click = get_row_col_from_click(click)
    return (c_click - 1) + (r_click - 1) * 8


def get_index_from_row_col(pos):
    """Given (row, col), return the index on the board"""
    return (pos[1] - 1) + (pos[0] - 1) * 8


def get_row_col_from_index(i: int) -> tuple:
    """Given an index from 0-63, return (row, col) as tuple"""
    col = (i % 8) + 1
    row = int((i + 1 - col) / 8) + 1
    return row, col


def get_blit_tuple_from_index(i, h):
    """Given an index on the board, returns the blit tuple"""
    row, col = get_row_col_from_index(i)
    # print(f"Index: {i}, (r, c): {row, col}")
    # print((col - 1) * 100, h - row * 100)
    return (col - 1) * 100, h - row * 100


def get_blit_tuple_from_row_col(rc, h):
    """Given (row, col), returns the blit tuple"""
    return (rc[1] - 1) * 100, h - rc[0] * 100


def king_is_in_check(board, color):
    """Given the current board and current piece color, return True if current color king is in check"""
    all_opposing_pieces = [p for p in board.squares if p and p.color != color]
    moves = []
    for piece in all_opposing_pieces:
        piece.calculate_moves(board)
        moves.extend(piece.possible_moves)

    king_pos = None
    for s in board.squares:
        if s and s.color == color and s.piece_type == "k":
            king_pos = get_row_col_from_index(s.board_index)

    if king_pos in moves:
        return True
    return False


def squares_threatened(b, color, square_list: list):
    moves = []
    for p in b.squares:
        if p and p.color != color:
            p.calculate_moves(b)
            moves.extend(p.possible_moves)
    for s in square_list:
        if s in moves:
            return True
    return False


def castling_moves_allowed(b, color) -> list:
    """Returns the list of castling moves allowed for the king of the given color"""
    allowed = []
    if color == "w" and not king_is_in_check(b, color):
        if b.squares[0] and not b.squares[0].moved and not b.squares[1] and not b.squares[2] and not b.squares[3]\
                and not squares_threatened(b, color, [(1, 3), (1, 4)]):
            allowed.append((1, 3))
        if b.squares[7] and not b.squares[7].moved and not b.squares[5] and not b.squares[6] \
                and not squares_threatened(b, color, [(1, 6), (1, 7)]):
            allowed.append((1, 7))
    elif color == "b" and not king_is_in_check(b, color):
        if b.squares[56] and not b.squares[56].moved and not b.squares[57] and not b.squares[58] and not b.squares[59] \
                and not squares_threatened(b, color, [(8, 3), (8, 4)]):
            allowed.append((8, 3))
        if b.squares[63] and not b.squares[63].moved and not b.squares[61] and not b.squares[62] \
                and not squares_threatened(b, color, [(8, 6), (8, 7)]):
            allowed.append((8, 7))
    return allowed

# and not squares_threatened(b, color, [(1, 3), (1, 4)])
