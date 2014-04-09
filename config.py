# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from pygame.sprite import RenderUpdates


'''
Módulo de configurações do jogo
Module game settings
'''


def config():
    pygame.init()  # inicializa o pygame
    Screen_Size = (800, 600)
    NAME = "Live In UNC" # Define name
    c_tela = pygame.display.set_mode(Screen_Size)  # Set map size
    pygame.display.set_caption(NAME)
    c_clock = pygame.time.Clock()
    c_background = pygame.image.load("img/Mao_map_new.png")
    c_tela.blit(c_background, (0, 0)) # copia a imagem de fundo para  o jogo
    return c_background, c_tela, c_clock
