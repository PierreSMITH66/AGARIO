import math
import random

import pygame

import core

from pygame.math import Vector2


class Avatar:
    def __init__(self, largeur=800, hauteur=450):
        self.nom = "ennemy1"
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon = 10
        self.rayonMAX = 150
        self.masse = 10
        self.speed = 10
        self.origine = Vector2(largeur/2, hauteur/2)
        self.force = Vector2(0, 0)
        self.vitesseMAX = 100
        self.vitesseMIN = 25
        self.accMAX = 0.5


    def move(self, creep):

        for p in creep:
            distance = p.position.distance_to(self.origine)
            a = distance.normalize()
        x = Vector2()
        v = Vector2((x - self.origine))
        u = v.normalize()
        if self.origine != x:
            vitesse = self.speed * u
            self.origine = self.origine + vitesse


    def show(self, screen):

            pygame.draw.circle(screen, self.couleur,self.origine, self.rayon)
            core.Draw.text((0, 0, 0), self.nom, self.origine)


    def manger(self, creep):
        for p in creep:
            if p.position.distance_to(self.origine) < self.rayon + p.taille:
                if p.vivant:
                    self.score += 10
                    if self.rayon < self.rayonMAX:
                        self.rayon += 0.5
                p.vivant = False
