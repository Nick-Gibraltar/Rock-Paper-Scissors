import pygame

pygame.init()

X_MAX = 2000
Y_MAX = 800
RED = (255,0,0)
BLACK = (0,0,0)
SCREEN = pygame.display.set_mode((X_MAX, Y_MAX))

def pygame_display_text(text_to_display, font_size, position, clear):
    text_style = pygame.font.Font('freesansbold.ttf', font_size)
    text = text_style.render(text_to_display, True, RED, BLACK)
    text_rect = text.get_rect()
    text_rect.topleft = position
    if clear:
        SCREEN.fill((0,0,0))
    SCREEN.blit(text, text_rect)
    pygame.display.flip()

def pygame_wait_for_spacebar():
    pressed=False
    while not pressed:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pressed=True