import random
import pygame
from pygame.math import Vector2


class Creep:

    def __init__(self, largeur=800, hauteur=450):
        self.rayon = 5
        self.origine = Vector2(random.randint(0+self.rayon, largeur-self.rayon), random.randint(0+self.rayon, hauteur-self.rayon))
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.masse = 10
        self.vivant = True

    def show(self, screen):
        if self.vivant :
            pygame.draw.circle(screen, self.couleur, self.origine, self.rayon)


