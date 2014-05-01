# -*- coding: utf-8 -*-

# Base/source code from Iury Alves' RPG-Pygame project
# Under MIT License
# https://github.com/IuryAlves/RPG-Pygame

import pygame
from pygame.locals import *
from pygame.sprite import RenderUpdates


'''
Module game settings
'''


def config():
    pygame.init()  # initialize pygame
    Screen_Size = (800, 600)
    NAME = "Live In UNC" # Define name
    c_screen = pygame.display.set_mode(Screen_Size)  # Set map size
    pygame.display.set_caption(NAME)
    c_clock = pygame.time.Clock()
    c_background = pygame.image.load("img/bg_map.png")
    c_screen.blit(c_background, (0, 0)) # copy image from background
    return c_background, c_screen, c_clock
