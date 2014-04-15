# -*- coding: utf-8 -*-

from config import *
from Classes import *
from Cores import *
import sys
from pygame.sprite import Sprite, RenderUpdates
FPS = 16

filaF, filaC, filaE, filaD = 0, 0, 0, 0

listaImagensFrente = ["sprites/RamesesD.png","sprites/RamesesD.png", "sprites/RamesesD.png"]
listaImagensLadoEsquerdo = ["sprites/RamesesL.png", "sprites/RamesesL.png", "sprites/RamesesL.png"]
listaImagensLadoDireito = ["sprites/RamesesR.png","sprites/RamesesR.png", "sprites/RamesesR.png"]
listaImagensCostas = ["sprites/RamesesU.png", "sprites/RamesesU.png", "sprites/RamesesU.png"]


listaImagens = [
listaImagensFrente,
listaImagensLadoEsquerdo,
listaImagensLadoDireito,
listaImagensCostas
]

# move player to left


def MPL(teclas,personagem):
    global filaE
    if teclas[K_LEFT] and not teclas[K_DOWN] and not teclas[K_UP]:
        personagem.image = pygame.image.load(listaImagensLadoEsquerdo[filaE])
        personagem.converterImagem()
        personagem.mover(-10, 0)
        personagem.px -= 1
        filaE += 1
        if filaE > 2:
            filaE = 0
#mover personagem para a direita


def MPR(teclas,personagem):
    global filaD
    if teclas[K_RIGHT] and not teclas[K_DOWN] and not teclas[K_UP]:
        personagem.image = pygame.image.load(listaImagensLadoDireito[filaD])
        personagem.converterImagem()
        personagem.mover(10, 0)
        personagem.px += 1
        filaD += 1
        if filaD > 2:
            filaD = 0

# mover plater up


def MPU(teclas,personagem):
    global filaC
    if teclas[K_UP]:
        personagem.image = pygame.image.load(listaImagensCostas[filaC])
        personagem.converterImagem()
        personagem.mover(0, -10)
        personagem.py -= 1
        filaC += 1
        if filaC > 2:
            filaC = 0

# mover personagem para baixo


def MPD(teclas,personagem):
    global filaF
    if teclas[K_DOWN]:
        personagem.image = pygame.image.load(listaImagensFrente[filaF])
        personagem.converterImagem()
        personagem.mover(0, 10)
        personagem.py += 1
        filaF += 1
        if filaF > 2:
            filaF = 0

#=======================

def main():
	fundo, tela, clock = config()

	#================================
	#Criação de objetos
	musica = pygame.mixer.Sound("BGM/Firelink Shrine.wav")
	grupo = RenderUpdates()
	personagem = Heroi(20, 290,['nome','sobrenome','classe'],listaImagens, grupo)
	npc = Npcs(650, 280, ['sprites/personagem2.png'], grupo)
	npc2 = Npcs(675, 240, ["sprites/personagem.png"], grupo)
	npc3 = Npcs(675, 340, ["sprites/personagem.png"], grupo)
	pygame.font.init()
	frase = Textos(40, 'Quem eh voce e oque faz aqui?', 'carolingia.ttf')

	#===================================

	lx = [b for b in range(-15, 30)]
	l1 = [-30]
	l2 = [30]

	#parede esquerda
	parede = [x for x in range(-10, 16)]
	#colisaoParedeLateral = Eventos(parede, -2)


	#===================================
	iniciarConversa = [52,6,36,-20,55,-10]

	teclas = {K_LEFT: False, K_RIGHT: False, K_UP: False, K_DOWN: False,
	          K_RETURN: False, 27: False}  # obs 27 = tecla 'esc'

	musica.play()
	fundo = fundo.convert()
	pygame.display.flip()
	while True:
	    clock.tick(FPS)

	    for e in pygame.event.get([KEYUP, KEYDOWN]):
	        valor = (e.type == KEYDOWN)
	        if e.key in teclas.keys():
	            teclas[e.key] = valor

	    if teclas[27]:  # tecla ESC
	        pygame.quit()
	        sys.exit()
	    if personagem.py in l1:  #player in the top
	        MPD(teclas,personagem)
	        MPR(teclas,personagem)
	        MPL(teclas,personagem)
	    elif personagem.py in l2: #player in the bottom
	        MPT(teclas,personagem)
	        MPR(teclas,personagem)
	        MPL(teclas,personagem)
	    else:
	        MPU(teclas,personagem)
	        MPD(teclas,personagem)
	        MPL(teclas,personagem)
	        MPR(teclas,personagem)

	    if personagem.px == iniciarConversa[0] and personagem.py == iniciarConversa[1]:
             import squirrel
             squirrel.main()
	    if personagem.px == iniciarConversa[2] and personagem.py == iniciarConversa[3]:
             import flippy
             flippy.main()
	    if personagem.px == iniciarConversa[4] and personagem.py == iniciarConversa[5]:
             import wormy
             wormy.main()
	    print(personagem.px, personagem.py)
        
	    grupo.clear(tela, fundo)
	    pygame.display.update(grupo.draw(tela))



if __name__ == '__main__':
	main()
