import random
import pygame
from pygame.math import Vector2


class Creep:

    def __init__(self, largeur=800, hauteur=450):
        self.taille = 5
        self.position = Vector2(random.randint(0+self.taille, largeur-self.taille), random.randint(0+self.taille, hauteur-self.taille))
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.masse = 10
        self.vivant = True

    def show(self, screen):
        if self.vivant :
            pygame.draw.circle(screen, self.couleur, [int(self.position.x), int(self.position.y)], self.taille)


