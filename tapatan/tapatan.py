import pygame
from pygame.image import load
from pygame.transform import scale
from pygame.display import flip, update

from webbrowser import open

from .constants import *
from .solvers import minimax
from .logic_game import TapatanGrid


class Tapatan:
    def __init__(self):
        # Initializing game logic
        self.player  = BLACK
        self.enemy   = WHITE
        self.tapatan = TapatanGrid()

        # Instantiating the font, clock, mixer and screen
        pygame.init()

        self.font   = pygame.font.SysFont(FONT_TYPE, size=FONT_SIZE, bold=True)
        self.clock  = pygame.time.Clock()
        self.sound  = pygame.mixer.music.load(GAME_MUSIC_PATH)
        self.screen = pygame.display.set_mode(SIZE)

        pygame.mixer.music.play(-1)
        pygame.display.set_caption('Tapatan')

        # Loading components used in the game
        self.bg = self.load_image(BG_PATH, SIZE)

        self.load_rects()
        self.load_piecs()
        self.load_board()

        self.button_play = self.load_image(PLAY_PATH, BP_SIZE)
        self.button_play_rect = self.button_play.get_rect(topleft=(SPC_L, BU_TOP))

        self.button_info = self.load_image(INFO_PATH, BU_SIZE)
        self.button_info_rect = self.button_info.get_rect(topright=(GRID_RIGHT, SPC))

        self.button_sound_on  = self.load_image(SOUND_ON_PATH, BU_SIZE)
        self.button_sound_off = self.load_image(SOUND_OFF_PATH, BU_SIZE)
        self.button_sound_rect = self.button_sound_on.get_rect(topright=(self.button_info_rect.left - SPC,
                                                                         self.button_info_rect.top))

        self.button_return = self.load_image(RETURN_PATH, BU_SIZE)
        self.button_return_rect = self.button_return.get_rect(topleft=self.button_sound_rect.topleft)

        self.button_refresh = self.load_image(REFRESH_PATH, BU_SIZE)
        self.button_refresh_rect = self.button_refresh.get_rect(topleft=self.button_info_rect.topleft)

        self.button_empty = self.load_image(EMPTY_PATH, BE_SIZE)
        self.button_time_rect  = self.button_empty.get_rect(topleft=(GRID_LEFT + SPC, BU_TOP))
        self.button_moves_rect = self.button_empty.get_rect(topright=(GRID_RIGHT - SPC, BU_TOP))

        self.button_win  = self.load_image(WIN_PATH , WIN_SIZE)
        self.button_lose = self.load_image(LOSE_PATH, WIN_SIZE)
        self.button_win_rect = self.button_win.get_rect(topleft=(GRID_LEFT, GRID_TOP + 2 * PIECE_SIDE))

    def init_game(self):
        while True:
            self.main_screen()
            self.play()

    def main_screen(self):
        self.display_main_screen()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    if self.button_play_rect.collidepoint(event.pos):
                        return
                    elif self.button_sound_rect.collidepoint(event.pos):
                        self.switch_sound()
                    elif self.button_info_rect.collidepoint(event.pos):
                        open('https://github.com/filipemedeiross', new=2)

    def play(self):
        time, moves, playing, start = self.init_variables()
        self.display_play_screen(time, moves)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_return_rect.collidepoint(event.pos):
                        self.tapatan.update()  # update the grid
                        return
                    elif self.button_refresh_rect.collidepoint(event.pos):
                        time, moves, playing, start = self.init_variables()
                        self.display_play_screen(time, moves)
                    elif playing:
                        pos, move = self.piece_collide(event.pos)

                        if move == START:
                            start = pos
                            self.display_board(start)
                        elif self.check_move(move, start, pos):
                            self.move(self.player, start, pos)
                            playing = self.check_win(self.player)

                            moves += 1
                            self.display_moves(moves)
                            
                            if playing:
                                time += self.minimax_move()
                                playing = self.check_win(self.enemy)

                                if playing:
                                    start = None

            if playing:
                time += self.clock.tick(FRAMERATE_PS)
                self.display_time(time)

    def display_main_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.button_play, self.button_play_rect)
        self.screen.blit(self.button_info, self.button_info_rect)

        self.display_sound()
        self.display_board()

        flip()

    def display_play_screen(self, time, moves):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.button_return, self.button_return_rect)
        self.screen.blit(self.button_refresh, self.button_refresh_rect)

        self.display_board()
        self.display_time(time)
        self.display_moves(moves)

        flip()

    def display_sound(self):
        self.screen.blit(self.button_sound_on
                         if self.play_sound
                         else self.button_sound_off,
                         self.button_sound_rect)

        update(self.button_sound_rect)

    def display_board(self, emp=None):
        self.screen.blit(self.board, self.board_rect)

        if emp:
            x, y = self.rects[(N * emp[0]) + emp[1]].topleft
            x += PIECE_CENTER
            y += PIECE_CENTER

            pygame.draw.circle(self.screen, EMPH_COLOR, (x, y), EMPHS_RADIUS)

        for usr, pos in zip(self.grid.flatten(), self.rects):
            if usr == BLACK:
                self.screen.blit(self.pieces[BLACK], pos.topleft)
            elif usr == WHITE:
                self.screen.blit(self.pieces[WHITE], pos.topleft)

        update(self.board_rect)

    def display_time(self, time):
        s = time // 1000
        time_text = self.font.render(f'{s // 60}:{s % 60}', True, FONT_COLOR)
        time_rect = time_text.get_rect(center=self.button_time_rect.center)

        self.screen.blit(self.button_empty, self.button_time_rect)
        self.screen.blit(time_text, time_rect)

        update(self.button_time_rect)

    def display_moves(self, moves):
        moves_text = self.font.render(f'{moves}', True, FONT_COLOR)
        moves_rect = moves_text.get_rect(center=self.button_moves_rect.center)

        self.screen.blit(self.button_empty, self.button_moves_rect)
        self.screen.blit(moves_text, moves_rect)

        update(self.button_moves_rect)

    def init_variables(self):
        time    = 0
        moves   = 0
        playing = True
        start   = None

        self.tapatan.update()
        self.clock.tick()

        return time, moves, playing, start
    
    def switch_sound(self):
        if self.play_sound:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

        self.display_sound()
    
    def piece_collide(self, event_pos):
        pos, move = None, None

        for x in range(N):
            for y in range(N):
                if self.rects[(x * N) + y].collidepoint(event_pos):
                    pos  = x, y

                    if self.tapatan[x, y] == self.player:                                    
                        move = START
                    elif self.tapatan[x, y] == EMPTY:
                        move = END
                    
        return pos, move
    
    def check_move(self, move, start, end):
        return move == END and \
               start       and \
               end in MOVES[start[0]][start[1]]
    
    def check_win(self, player):
        playing = True

        if self.tapatan.win(player):
            playing = False

            if player == self.player:
                self.screen.blit(self.button_win, self.button_win_rect)
            else:
                self.screen.blit(self.button_lose, self.button_win_rect)

            update(self.button_win_rect)
        
        return playing
    
    def move(self, player, start, pos):
        self.tapatan.move(player, start, pos)
        self.display_board()

    def minimax_move(self):
        time = pygame.time.wait(1000)

        self.move(self.enemy, *minimax(self.grid))

        return time

    def load_rects(self):
        self.rects = [pygame.Rect(GRID_LEFT + PIECE_SPC * j,
                                  GRID_TOP  + PIECE_SPC * i,
                                  PIECE_SIDE, PIECE_SIDE)
                      for i in range(N)
                      for j in range(N)]

    def load_piecs(self):
        self.pieces = {BLACK : self.load_image(BLACK_PATH, PIECE_SIZE),
                       WHITE : self.load_image(WHITE_PATH, PIECE_SIZE)}

    def load_board(self):
        self.board = self.bg.subsurface(self.rects[0].topleft, GRID_SIZE)
        self.board_rect = self.board.get_rect(topleft=self.rects[0].topleft)

        for x0 in range(N):
            for y0 in range(N):
                pos_x0, pos_y0 = self.rects[(N * x0) + y0].topleft
                pos_x0 += SPC_X
                pos_y0 += SPC_Y

                pygame.draw.circle(self.board, GRID_COLOR, (pos_x0, pos_y0), PIECE_RADIUS)

                for x1, y1 in MOVES[x0][y0]:
                    pos_x1, pos_y1 = self.rects[(N * x1) + y1].topleft
                    pos_x1 += SPC_X
                    pos_y1 += SPC_Y

                    pygame.draw.line(self.board, GRID_COLOR, (pos_x0, pos_y0), (pos_x1, pos_y1), W_LINE)

    @staticmethod
    def load_image(path, size):
        return scale(load(path), size)

    @property
    def grid(self):
        return self.tapatan.grid

    @property
    def play_sound(self):
        return pygame.mixer.music.get_busy()
