import pygame

pygame.mixer.init()

pygame.mixer.music.load("sonidos/musica.mp3")
pygame.mixer.music.play(-1)

input("Presiona ENTER para detener...")

pygame.mixer.music.stop()
pygame.quit()