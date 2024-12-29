import pygame

pygame.mixer.init()
pygame.mixer.music.load('ig.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busey():
    continue