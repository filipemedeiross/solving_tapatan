import pygame
from webbrowser import open
from .logic_game import TapatanGrid
from .constants import *


class Tapatan:
    def __init__(self):
        pygame.init()

        self.tapatan = TapatanGrid()

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

        self.button_play = pygame.image.load('tapatan/media/play.png')
        self.button_play = pygame.transform.scale(self.button_play, (w_button_play, h_button_play))
        self.button_play_rect = self.button_play.get_rect(topleft=(spacing_lateral, spacing_button_bottom))

        self.button_info = pygame.image.load('tapatan/media/info.png')
        self.button_info = pygame.transform.scale(self.button_info, (w_button, h_button))
        self.button_info_rect = self.button_info.get_rect(topright=(width - spacing_grid_lateral, spacing))

        self.button_sound = pygame.image.load('tapatan/media/sound.png')
        self.button_sound = pygame.transform.scale(self.button_sound, (w_button, h_button))
        self.button_sound_rect = self.button_sound.get_rect(topright=(self.button_info_rect.left - spacing, spacing))

        self.button_sound_off = pygame.image.load('tapatan/media/sound_off.png')
        self.button_sound_off = pygame.transform.scale(self.button_sound_off, (w_button, h_button))

    # Method that start the game
    def init_game(self):
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Tapatan')

        self.playing_music = True
        pygame.mixer.music.play(loops=-1)

        while True:
            self.main_screen()

    def main_screen(self):
        # Preparing the main screen
        self.screen.blit(self.background, (0, 0))

        self.screen.blit(self.button_play, self.button_play_rect)
        self.screen.blit(self.button_info, self.button_info_rect)

        self.display_sound()
        self.display_board()

        pygame.display.flip()

        # Getting input from user
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_play_rect.collidepoint(event.pos):
                        return
                    elif self.button_sound_rect.collidepoint(event.pos):
                        self.switch_sound()
                        self.display_sound()
                    elif self.button_info_rect.collidepoint(event.pos):
                        open('https://github.com/filipemedeiross', new=2)
            
            self.clock.tick(10)

    def display_board(self):
        self.screen.blit(self.background,
                         self.rects[0],
                        (self.rects[0], (grid, grid)))

        for x0 in range(N):
            for y0 in range(N):
                for x1, y1 in MOVES[x0][y0]:
                    x_start, y_start = self.rects[(x0 * N) + y0]
                    x_start += spacing_piece_center
                    y_start += spacing_piece_center

                    x_end, y_end = self.rects[(x1 * N) + y1]
                    x_end += spacing_piece_center
                    y_end += spacing_piece_center

                    pygame.draw.line(self.screen, COLOR_GRID, (x_start, y_start), (x_end, y_end), w_grid_line)

        for user, pos in zip(self.tapatan.grid.flatten(), self.rects):
            if user == BLACK:
                self.screen.blit(self.pieces[BLACK], pos)
            elif user == WHITE:
                self.screen.blit(self.pieces[WHITE], pos)
            elif user == EMPTY:
                x, y = pos
                x += spacing_piece_center
                y += spacing_piece_center
                
                pygame.draw.circle(self.screen, COLOR_GRID, (x, y), radius_piece_empty)

    def display_sound(self):
        if self.playing_music:
            self.screen.blit(self.button_sound, self.button_sound_rect)
        else:
            self.screen.blit(self.button_sound_off, self.button_sound_rect)
        
        pygame.display.update(self.button_sound_rect)

    def switch_sound(self):
        if self.playing_music:
            pygame.mixer.music.pause()
            self.playing_music = False
        else:
            pygame.mixer.music.unpause()
            self.playing_music = True

    def load_pieces(self):
        pieces = {BLACK : pygame.image.load(f'tapatan/media/black_piece.png'),
                  WHITE : pygame.image.load(f'tapatan/media/white_piece.png')}
        
        pieces[BLACK] = pygame.transform.scale(pieces[BLACK], (size_piece, size_piece))
        pieces[WHITE] = pygame.transform.scale(pieces[WHITE], (size_piece, size_piece))

        return pieces
    
    def load_rects(self):
        rects = []

        for i in range(N):
            for j in range(N):
                rects.append((spacing_grid_lateral + (2.5*size_piece) * j,
                              spacing_grid_top     + (2.5*size_piece) * i))
        
        return rects


if __name__ == '__main__':
    tapatan = Tapatan()
    tapatan.init_game()
