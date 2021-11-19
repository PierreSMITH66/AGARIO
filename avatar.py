import random

import pygame

import core

from pygame.math import Vector2


class Avatar:
    def __init__(self, largeur=800, hauteur=450):
        self.nom
        self.score = 0
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon = 10
        self.masse = 10
        self.vitesse = Vector2(0, 0)
        self.origine = Vector2(largeur/2, hauteur/2)
        self.force = Vector2(0, 0)
        self.vitesseMAX = 100
        self.vitesseMIN = 25
        self.tailleMAX = 300
        self.accMAX = 0.5
        self.k = 0.001
        self.l0 = 10



    def move(self):
       '''Bilan des Forces'''
       x = Vector2(core.getMouseLeftClick())
       v = Vector2((x - self.origine))
       u = v.normalize()
       l = v.length()
       fr = Vector2(self.k * (l - self.l0) * u)

       '''Vecteur Vitesse'''

       self.vitesse = self.vitesse + fr
       fr = Vector2(0, 0)

       '''DEPLACEMENT'''
       self.origine = self.origine + self.vitesse



    def show(self,screen):
        pygame.draw.circle(screen, self.couleur, [int(self.position.x), int(self.position.y)], self.taille)
