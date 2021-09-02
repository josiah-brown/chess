from piece import Piece

# Stores the starting board as a  list of pieces
starting_positions = [
        Piece("assets/wr.png", 1, 1, "r", "w"),  # index 0
        Piece("assets/wn.png", 1, 2, "n", "w"),
        Piece("assets/wb.png", 1, 3, "b", "w"),
        Piece("assets/wq.png", 1, 4, "q", "w"),
        Piece("assets/wk.png", 1, 5, "k", "w"),
        Piece("assets/wb.png", 1, 6, "b", "w"),
        Piece("assets/wn.png", 1, 7, "n", "w"),
        Piece("assets/wr.png", 1, 8, "r", "w"),  # index 7

        Piece("assets/wp.png", 2, 1, "p", "w"),
        Piece("assets/wp.png", 2, 2, "p", "w"),
        Piece("assets/wp.png", 2, 3, "p", "w"),
        Piece("assets/wp.png", 2, 4, "p", "w"),
        Piece("assets/wp.png", 2, 5, "p", "w"),
        Piece("assets/wp.png", 2, 6, "p", "w"),
        Piece("assets/wp.png", 2, 7, "p", "w"),
        Piece("assets/wp.png", 2, 8, "p", "w"),  # index 15

        None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None,

        Piece("assets/bp.png", 7, 1, "p", "b"),
        Piece("assets/bp.png", 7, 2, "p", "b"),
        Piece("assets/bp.png", 7, 3, "p", "b"),
        Piece("assets/bp.png", 7, 4, "p", "b"),
        Piece("assets/bp.png", 7, 5, "p", "b"),
        Piece("assets/bp.png", 7, 6, "p", "b"),
        Piece("assets/bp.png", 7, 7, "p", "b"),
        Piece("assets/bp.png", 7, 8, "p", "b"),

        Piece("assets/br.png", 8, 1, "r", "b"),
        Piece("assets/bn.png", 8, 2, "n", "b"),
        Piece("assets/bb.png", 8, 3, "b", "b"),
        Piece("assets/bq.png", 8, 4, "q", "b"),
        Piece("assets/bk.png", 8, 5, "k", "b"),
        Piece("assets/bb.png", 8, 6, "b", "b"),
        Piece("assets/bn.png", 8, 7, "n", "b"),
        Piece("assets/br.png", 8, 8, "r", "b")  # index 63
]
