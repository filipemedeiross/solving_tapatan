from pygame.locals import *


# Logic settings

N = 3
DEPTH = 4

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

WINNING_POS = [[(0, 0), (0, 1), (0, 2)],
               [(1, 0), (1, 1), (1, 2)],
               [(2, 0), (2, 1), (2, 2)],
               [(0, 0), (1, 0), (2, 0)],
               [(0, 1), (1, 1), (2, 1)],
               [(0, 2), (1, 2), (2, 2)],
               [(0, 0), (1, 1), (2, 2)],
               [(0, 2), (1, 1), (2, 0)]]

# Game settings

TIME_WAIT = 1000
FRAMERATE_PS = 10

FONT_TYPE = 'Arial'
FONT_SIZE = 20

FONT_COLOR = 0, 0, 0
GRID_COLOR = 184, 134, 11
EMPH_COLOR = 135, 206, 235

BG_PATH         = 'tapatan/media/bg.png'
WIN_PATH        = 'tapatan/media/win.png'
LOSE_PATH       = 'tapatan/media/lose.png'
PLAY_PATH       = 'tapatan/media/play.png'
INFO_PATH       = 'tapatan/media/info.png'
BLACK_PATH      = 'tapatan/media/black.png'
WHITE_PATH      = 'tapatan/media/white.png'
EMPTY_PATH      = 'tapatan/media/empty.png'
RETURN_PATH     = 'tapatan/media/return.png'
REFRESH_PATH    = 'tapatan/media/refresh.png'
SOUND_ON_PATH   = 'tapatan/media/sound_on.png'
SOUND_OFF_PATH  = 'tapatan/media/sound_off.png'
GAME_MUSIC_PATH = 'tapatan/media/desert_song.mp3'

# Dimensions of screen elements

SIZE = WIDTH, HEIGHT = 240, 360

BU_TOP     = HEIGHT * 3 / 4
GRID_TOP   = 60
GRID_LEFT  = 25
GRID_RIGHT = WIDTH - GRID_LEFT

W_LINE = 5
W_GRID = WIDTH - 2 * GRID_LEFT
GRID_SIZE = W_GRID, W_GRID

PIECE_SIDE = W_GRID / (2 * N)
PIECE_SPC  = 2.5 * PIECE_SIDE
PIECE_SIZE = PIECE_SIDE, PIECE_SIDE
PIECE_CENTER = PIECE_SIDE / 2
PIECE_RADIUS = PIECE_SIDE / 4
EMPHS_RADIUS = PIECE_CENTER

SPC = 10
SPC_L = 15
SPC_X = PIECE_CENTER - GRID_LEFT
SPC_Y = PIECE_CENTER - GRID_TOP

BU_SIZE = W_BU, H_BU = 35, 35
BP_SIZE = W_BP, H_BP = WIDTH - 2 * SPC_L, H_BU
BE_SIZE = FONT_SIZE * 4, FONT_SIZE * 3 / 2
WIN_SIZE = W_GRID, W_GRID / 3
