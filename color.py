from controller import Controller
from controller import cols_to_col
import numpy as np
import pygame, sys, colorsys

pygame.init()

con = Controller()

display = pygame.display.set_mode((256, 256))

basecol = [0, 1, 1]
col = basecol
update = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                pos = event.pos
                col[1] = (256-pos[0])/256
                col[2] = (256-pos[1])/256
        elif event.type == pygame.MOUSEWHEEL:
            col[0] += event.y/360
            if col[0] > 1: col[0] = 0
            elif col[0] < 0: col[0] = 1
            update = True
    
    n_rgb = colorsys.hsv_to_rgb(*col)
    rgb = [round(n_rgb[0]*255), round(n_rgb[1]*255), round(n_rgb[2]*255)]
    cin = cols_to_col(*rgb)
    print(col, rgb)
    con.send(cin, wait=(1/60)*1000, log=False)

    if update:
        update = False
        display.fill((0, 0, 0))
        for x in range(256):
            for y in range(256):
                n_rgb = colorsys.hsv_to_rgb(col[0], (256-x)/256, (256-y)/256)
                rgb = [round(n_rgb[0]*255), round(n_rgb[1]*255), round(n_rgb[2]*255)]
                display.set_at((x, y), rgb)
        pygame.display.flip()