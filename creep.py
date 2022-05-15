import random
import pygame
import core
from pygame.math import Vector2


class Creep:

    def __init__(self, largeur=1600, hauteur=900):
        self.rayon = 5
        self.rayonInit = self.rayon
        self.origine = Vector2(random.randint(0+self.rayon, largeur-self.rayon), random.randint(0+self.rayon, hauteur-self.rayon))
        self.couleur = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        self.masse = 10
        self.vivant = True

    def show(self, screen):
            pygame.draw.circle(screen, self.couleur, self.origine, self.rayon)

    def death(self, largeur=1600, hauteur=900):
        if core.memory("tempoc") != 500:
            core.memory("tempoc", core.memory("tempoc") + 1)
        else:
            core.memory("tempoc", 0)
            self.rayon = self.rayonInit
            self.vivant = True
            self.origine = Vector2(random.randint(0 + self.rayon, largeur - self.rayon), random.randint(0 + self.rayon, hauteur - self.rayon))
