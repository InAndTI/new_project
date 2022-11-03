import pygame
import math
from CONST import *

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((OX, OY), pygame.RESIZABLE)
pygame.display.set_caption('engl')
clock = pygame.time.Clock()
text = ''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
        if event.type == pygame.MOUSEMOTION:
            pass
    # key = pygame.key.get_pressed()
    # if key[pygame.K_BACKSPACE]:
    #     text = text[:-1]

    font = pygame.font.Font(None, 50)
    text_draw = font.render(text, True, (0, 100, 0))
    sc.fill((255, 255, 255))
    place = text_draw.get_rect(
        center=(OX//2, OY*3//4))
    sc.blit(text_draw, place)
    clock.tick(FPS)
    pygame.display.update()
