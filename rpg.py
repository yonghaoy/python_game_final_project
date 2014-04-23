# -*- coding: utf-8 -*-

# Base/source code from Iury Alves' RPG-Pygame project
# Under MIT License
# https://github.com/IuryAlves/RPG-Pygame

from config import *
from Classes import *
from Cores import *
import sys
from pygame.sprite import Sprite, RenderUpdates
FPS = 16

rowF, rowC, rowE, rowD = 0, 0, 0, 0

listImagensFrente = ["sprites/RamesesD.png","sprites/RamesesD.png", "sprites/RamesesD.png"]
listImagensLadoEsquerdo = ["sprites/RamesesL.png", "sprites/RamesesL.png", "sprites/RamesesL.png"]
listImagensLadoDireito = ["sprites/RamesesR.png","sprites/RamesesR.png", "sprites/RamesesR.png"]
listImagensCostas = ["sprites/RamesesU.png", "sprites/RamesesU.png", "sprites/RamesesU.png"]


listImagens = [
listImagensFrente,
listImagensLadoEsquerdo,
listImagensLadoDireito,
listImagensCostas
]

# move player to left


def MPL(keys,personagem):
	global rowE
	if keys[K_LEFT] and not keys[K_DOWN] and not keys[K_UP]:
		personagem.image = pygame.image.load(listImagensLadoEsquerdo[rowE])
		personagem.converterImagem()
		personagem.mover(-10, 0)
		personagem.px -= 1
		rowE += 1
		if rowE > 2:
			rowE = 0
#move player right


def MPR(keys,personagem):
	global rowD
	if keys[K_RIGHT] and not keys[K_DOWN] and not keys[K_UP]:
		personagem.image = pygame.image.load(listImagensLadoDireito[rowD])
		personagem.converterImagem()
		personagem.mover(10, 0)
		personagem.px += 1
		rowD += 1
		if rowD > 2:
			rowD = 0

# mover player up


def MPU(keys,personagem):
	global rowC
	if keys[K_UP]:
		personagem.image = pygame.image.load(listImagensCostas[rowC])
		personagem.converterImagem()
		personagem.mover(0, -10)
		personagem.py -= 1
		rowC += 1
		if rowC > 2:
			rowC = 0

# mover personagem para baixo


def MPD(keys,personagem):
	global rowF
	if keys[K_DOWN]:
		personagem.image = pygame.image.load(listImagensFrente[rowF])
		personagem.converterImagem()
		personagem.mover(0, 10)
		personagem.py += 1
		rowF += 1
		if rowF > 2:
			rowF = 0

#=======================

def main():
	background, screen, clock = config()

	#================================
	#Criação de objetos
	musica = pygame.mixer.Sound("BGM/hark_the_sound.wav")
	group = RenderUpdates()
	personagem = Heroi(20, 290,['nome','sobrenome','classe'],listImagens, group)
	npc = Npcs(650, 280, ['sprites/personagem2.png'], group)
	npc2 = Npcs(675, 240, ["sprites/personagem.png"], group)
	npc3 = Npcs(675, 340, ["sprites/personagem.png"], group)
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

	keys = {K_LEFT: False, K_RIGHT: False, K_UP: False, K_DOWN: False,
			  K_RETURN: False, 27: False}  # obs 27 = key 'esc'

	musica.play()
	background = background.convert()
	pygame.display.flip()
	while True:
		clock.tick(FPS)

		for e in pygame.event.get([KEYUP, KEYDOWN]):
			valor = (e.type == KEYDOWN)
			if e.key in keys.keys():
				keys[e.key] = valor

		if keys[27]:  # key ESC
			pygame.quit()
			sys.exit()
		if personagem.py in l1:  #player in the top
			MPD(keys,personagem)
			MPR(keys,personagem)
			MPL(keys,personagem)
		elif personagem.py in l2: #player in the bottom
			MPT(keys,personagem)
			MPR(keys,personagem)
			MPL(keys,personagem)
		else:
			MPU(keys,personagem)
			MPD(keys,personagem)
			MPL(keys,personagem)
			MPR(keys,personagem)

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
		
		group.clear(screen, background)
		pygame.display.update(group.draw(screen))



if __name__ == '__main__':
	main()
