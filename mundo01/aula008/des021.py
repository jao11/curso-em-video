# Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
import pygame
print('Gostariamos que você ouvisse essa música')
pygame.mixer.init()
pygame.mixer.music.load('des021.mp3')
pygame.mixer.music.play()
print('Por favor ouça...')
input('Para parar digite algo e de enter:')
