""" Faça um programa em Pyhton que abra e reproduza o áudio de um arquivo mp3 """

# Importando o módulo pygame
import pygame

# Importando timer
import time

# Iniciando o mixer
pygame.init()

# Carregando a música
pygame.mixer.music.load('mp3/lucasbeat.mp3')

# Reporduzindo a música
pygame.mixer.music.play()

# Tempo de reprodução da música
time.sleep(360)
