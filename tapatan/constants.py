# Logic settings

N = 3

EMPTY = 0
BLACK = 1
WHITE = 2
START = 3
END   = 4

MOVES =  [[[(0, 1), (1, 0), (1, 1)],
           [(0, 0), (0, 2), (1, 1)],
           [(0, 1), (1, 1), (1, 2)]],
          [[(0, 0), (1, 1), (2, 0)],
           [(0, 0), (0, 1), (0, 2),
            (1, 0), (1, 2), (2, 0),
            (2, 1), (2, 2)],
           [(0, 2), (1, 1), (2, 2)]],
          [[(1, 0), (1, 1), (2, 1)],
           [(1, 1), (2, 0), (2, 2)],
           [(1, 1), (1, 2), (2, 1)]]]

WINNING_POSITIONS = [[(0, 0), (0, 1), (0, 2)],
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     [(0, 0), (1, 0), (2, 0)],
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     [(0, 0), (1, 1), (2, 2)],
                     [(0, 2), (1, 1), (2, 0)]]

# Colors

COLOR_FONT = 0, 0, 0
COLOR_GRID = 184, 134, 11
COLOR_EMPH = 135, 206, 235

# Dimensions

size = width, height = 240, 360
font_size = 20 

spacing = 10
spacing_lateral = 15

spacing_grid_top   = 60
spacing_grid_left  = 25
spacing_grid_right = width - spacing_grid_left
spacing_button_bottom = height * 3 / 4

grid = width - 2 * spacing_grid_left
w_grid_line = 5

side_piece = grid / (2 * N)
size_piece = side_piece, side_piece
spacing_piece_center = side_piece / 2
radius_piece_empty   = side_piece / 4
radius_emphasis      = spacing_piece_center

size_button       = w_button, h_button = 35, 35
size_button_play  = w_button_play, h_button_play = width - 2 * spacing_lateral, h_button
size_button_empty = font_size * 4, font_size * 3 / 2
size_message_win  = grid, grid / 3
