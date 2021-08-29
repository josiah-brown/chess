
def get_position_from_click(click) -> tuple:
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