import pygame
from webbrowser import open
from .constants import *
from .logic_game import TapatanGrid
from .solvers import minimax


class Tapatan:
    def __init__(self):
        pygame.init()

        self.tapatan = TapatanGrid()
        self.player  = BLACK
        self.enemy   = WHITE

        self.screen = None
        self.font   = pygame.font.SysFont('Arial', size=font_size, bold=True)
        self.clock  = pygame.time.Clock()
        self.sound  = pygame.mixer.music.load('tapatan/media/desert_song.mp3')

        self.playing_music = None

        # Loading components used in the game
        self.pieces = self.load_pieces()      
        self.rects  = self.load_rects()

        self.background = pygame.image.load('tapatan/media/bg.png')
        self.background = pygame.transform.scale(self.background, size)

        self.board = self.load_board()
        self.board_rect = self.board.get_rect(topleft=self.rects[0].topleft)

        self.button_play = pygame.image.load('tapatan/media/play.png')
        self.button_play = pygame.transform.scale(self.button_play, size_button_play)
        self.button_play_rect = self.button_play.get_rect(topleft=(spacing_lateral, spacing_button_bottom))

        self.button_info = pygame.image.load('tapatan/media/info.png')
        self.button_info = pygame.transform.scale(self.button_info, size_button)
        self.button_info_rect = self.button_info.get_rect(topright=(spacing_grid_right, spacing))

        self.button_sound = pygame.image.load('tapatan/media/sound.png')
        self.button_sound = pygame.transform.scale(self.button_sound, size_button)
        self.button_sound_off = pygame.image.load('tapatan/media/sound_off.png')
        self.button_sound_off = pygame.transform.scale(self.button_sound_off, size_button)
        self.button_sound_rect = self.button_sound.get_rect(topright=(self.button_info_rect.left - spacing, self.button_info_rect.top))

        self.button_refresh = pygame.image.load('tapatan/media/refresh.png')
        self.button_refresh = pygame.transform.scale(self.button_refresh, size_button)
        self.button_refresh_rect = self.button_refresh.get_rect(topleft=self.button_info_rect.topleft)

        self.button_return = pygame.image.load('tapatan/media/return.png')
        self.button_return = pygame.transform.scale(self.button_return, size_button)
        self.button_return_rect = self.button_return.get_rect(topleft=self.button_sound_rect.topleft)

        self.button_empty = pygame.image.load('tapatan/media/empty.png')
        self.button_empty = pygame.transform.scale(self.button_empty, size_button_empty)
        self.button_time_rect = self.button_empty.get_rect(topleft=(spacing_grid_left + spacing, spacing_button_bottom))
        self.button_moves_rect = self.button_empty.get_rect(topright=(spacing_grid_right - spacing, spacing_button_bottom))
    
        self.button_win = pygame.image.load('tapatan/media/win.png')
        self.button_win = pygame.transform.scale(self.button_win, size_message_win)
        self.button_lose = pygame.image.load('tapatan/media/lose.png')
        self.button_lose = pygame.transform.scale(self.button_lose, size_message_win)
        self.button_win_rect = self.button_win.get_rect(topleft=(spacing_grid_left, spacing_grid_top + 2 * side_piece))

    # Method that start the game
    def init_game(self):
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Tapatan')

        self.playing_music = True
        pygame.mixer.music.play(-1)

        while True:
            self.main_screen()
            self.play()

    def main_screen(self):
        # Preparing the main screen
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.button_play, self.button_play_rect)
        self.screen.blit(self.button_info, self.button_info_rect)

        self.display_board()
        self.display_sound()

        pygame.display.flip()

        # Getting input from user
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_play_rect.collidepoint(event.pos):
                        return
                    elif self.button_sound_rect.collidepoint(event.pos):
                        self.switch_sound()
                        self.display_sound()
                    elif self.button_info_rect.collidepoint(event.pos):
                        open('https://github.com/filipemedeiross', new=2)

    def play(self):
        self.screen.blit(self.background, (0, 0))  # overriding main screen buttons
        self.screen.blit(self.button_return, self.button_return_rect)
        self.screen.blit(self.button_refresh, self.button_refresh_rect)

        pygame.display.flip()

        time, moves, playing, start = self.init_variables()
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
                time += self.clock.tick(10)
                self.display_time(time)

    def display_board(self, emphasis=None):
        self.screen.blit(self.board, self.board_rect)

        if emphasis:
            x_emph, y_emph = self.rects[(emphasis[0] * N) + emphasis[1]].topleft
            x_emph += spacing_piece_center
            y_emph += spacing_piece_center

            pygame.draw.circle(self.screen, COLOR_EMPH, (x_emph, y_emph), radius_emphasis)

        for user, pos in zip(self.tapatan.grid.flatten(), self.rects):
            if user == BLACK:
                self.screen.blit(self.pieces[BLACK], pos.topleft)
            elif user == WHITE:
                self.screen.blit(self.pieces[WHITE], pos.topleft)

        pygame.display.update(self.board_rect)

    def display_sound(self):
        if self.playing_music:
            self.screen.blit(self.button_sound, self.button_sound_rect)
        else:
            self.screen.blit(self.button_sound_off, self.button_sound_rect)
        
        pygame.display.update(self.button_sound_rect)

    def display_moves(self, moves):
        moves_text = self.font.render(f'{moves}', True, COLOR_FONT)

        self.screen.blit(self.button_empty, self.button_moves_rect)
        self.screen.blit(moves_text, (self.button_moves_rect.centerx - (moves_text.get_width() / 2),
                                      self.button_moves_rect.centery - (moves_text.get_height() / 2)))
        
        pygame.display.update(self.button_moves_rect)

    def display_time(self, time):
        time_text = self.font.render(f'{time // 1000 // 60}:{time // 1000 % 60}', True, COLOR_FONT)

        self.screen.blit(self.button_empty, self.button_time_rect)
        self.screen.blit(time_text, (self.button_time_rect.centerx - (time_text.get_width() / 2),
                                     self.button_time_rect.centery - (time_text.get_height() / 2)))

        pygame.display.update(self.button_time_rect)

    def init_variables(self):
        time    = 0
        moves   = 0
        playing = True
        start   = None

        self.tapatan.update()
        self.clock.tick()
        
        self.display_board()
        self.display_time(time)
        self.display_moves(moves)

        return time, moves, playing, start
    
    def switch_sound(self):
        if self.playing_music:
            pygame.mixer.music.pause()
            self.playing_music = False
        else:
            pygame.mixer.music.unpause()
            self.playing_music = True
    
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

            pygame.display.update(self.button_win_rect)
        
        return playing
    
    def move(self, player, start, pos):
        self.tapatan.move(player, start, pos)
        self.display_board()

    def minimax_move(self):
        time = pygame.time.wait(1000)

        self.move(self.enemy, *minimax(self.tapatan.grid))

        return time

    def load_pieces(self):
        pieces = {BLACK : pygame.image.load('tapatan/media/black_piece.png'),
                  WHITE : pygame.image.load('tapatan/media/white_piece.png')}
        
        pieces[BLACK] = pygame.transform.scale(pieces[BLACK], size_piece)
        pieces[WHITE] = pygame.transform.scale(pieces[WHITE], size_piece)

        return pieces
    
    def load_rects(self):
        rects = []

        for i in range(N):
            for j in range(N):
                topleft = (spacing_grid_left + (2.5*side_piece) * j,
                           spacing_grid_top  + (2.5*side_piece) * i)
                
                rects.append(pygame.Rect(topleft, size_piece))
        
        return rects
    
    def load_board(self):
        board = self.background.subsurface(self.rects[0].topleft, (grid, grid))

        spacing_x = spacing_piece_center - self.rects[0].left
        spacing_y = spacing_piece_center - self.rects[0].top

        for x0 in range(N):
            for y0 in range(N):
                x_start, y_start = self.rects[(x0 * N) + y0].topleft
                x_start += spacing_x
                y_start += spacing_y
                
                pygame.draw.circle(board, COLOR_GRID, (x_start, y_start), radius_piece_empty)

                for x1, y1 in MOVES[x0][y0]:
                    x_end, y_end = self.rects[(x1 * N) + y1].topleft
                    x_end += spacing_x
                    y_end += spacing_y

                    pygame.draw.line(board, COLOR_GRID, (x_start, y_start), (x_end, y_end), w_grid_line)

        return board


if __name__ == '__main__':
    tapatan = Tapatan()
    tapatan.init_game()
