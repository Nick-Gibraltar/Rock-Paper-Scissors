"""
Functions using the Pygame library to display text and
wait for the spacebar to be pressed.

Separated into another file for clarity.
"""
import pygame

pygame.init()

X_MAX = 2000
Y_MAX = 800
RED = (255,0,0)
BLACK = (0,0,0)
SCREEN = pygame.display.set_mode((X_MAX, Y_MAX))

def pygame_display_text(text_to_display, font_size, position, clear):
    """
    A function to display text to the Pygame display surface
    
    Parameters
    text_to_display : str
        a string containing text to display
    font_size : int
        the size of the text to be displayed
    position : (int, int)
        a tuple containing the x and y coordinates of the position of text
    clear : bool
        True if the display is cleared before new text is printed, False if it isn't

    """
    text_style = pygame.font.Font('freesansbold.ttf', font_size)
    text = text_style.render(text_to_display, True, RED, BLACK)
    text_rect = text.get_rect()
    text_rect.topleft = position
    if clear:
        SCREEN.fill((0,0,0))
    SCREEN.blit(text, text_rect)
    pygame.display.flip()

def pygame_wait_for_spacebar():
    """
    A function using Pygame to wait for the spacebar to be pressed
    """
    pressed=False
    while not pressed:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pressed=True