# -*- coding: utf-8 -*-

# Base/source code from Iury Alves' RPG-Pygame project
# Under MIT License
# https://github.com/IuryAlves/RPG-Pygame

try:
  import pygame
except Exception:
  print("no pygame found")

from pygame.locals import *
from pygame.sprite import Sprite
from Cores import *
                      

#Classes

class Personagens(Sprite):
  '''
   *rowImagens sao as imagens reference ao personagem'''

  def __init__(self, pxInicial, pyInicial,rowImagens, *groups):
        Sprite.__init__(self, *groups)
        self.pxInicial = pxInicial
        self.pyInicial = pyInicial
        self.px = 0
        self.py = 0
        self.rect = Rect(self.pxInicial, self.pyInicial, 0, 0)
        self.image = pygame.image.load(rowImagens[0])

        self.image.convert_alpha()
        self.image.set_colorkey(magenta, RLEACCEL) #coloca a cor magenta como transparente
        pygame.draw.rect(self.image, black, self) #Desenha a imagem na tela

  def mover(self, x, y):
    self.rect.move_ip(x, y)

  def converterImagem(self):
    self.image.convert_alpha()


class Heroi(Personagens):
  ''' classe que contem os dados do nosso herói
  '''

  def __init__(self,pxInicial, pyInicial,dados,rowImagens, *groups):
    Personagens.__init__(self,pxInicial, pyInicial,rowImagens, *groups)
    self.nome = dados[0]
    self.vida = dados[1]
    self.classe = dados[2]    


class Npcs(Personagens):
  '''
  classe que contem os dados dos Npcs
  '''

  def __init__(self,pxInicial,pyInicial,rowImagens,*groups):
    Personagens.__init__(self,pxInicial,pyInicial,rowImagens,*groups)


class Textos():
    '''
    Classe que gerencia todos os textos do jogo.Class that manages all texts in the game
    '''

    def __init__(self, tamanho, dialogo, arquivoDeFonte, cor=white, antialias=True):  # antialias faz um tratamento na imagem
        #pygame.font.init()
        self.tamanho = tamanho  # tamanho da frase
        self.dialogo = dialogo  # frase
        self.cor = cor  # cor
        self.antialias = antialias
        self.fonte = pygame.font.SysFont(arquivoDeFonte, self.tamanho)
        self.frases = self.fonte.render(
            self.dialogo, self.antialias, self.cor)

    def alterarDialogo(self, novodialogo):
        self.dialogo = novodialogo

    def alterarCor(self, novaCor):
        self.cor = novaCor

    def alterarTamanho(self, novoTamanho):
        self.tamanho = novoTamanho


class Pontos(object):
  '''
  define um array de  posicoes no mapa em que o personagem pode passar
  '''
  def __init__(self,*pontos):
    self.pontos = pontos
    self.pontosX = pontos[0]
    self.pontosY = pontos[1]
