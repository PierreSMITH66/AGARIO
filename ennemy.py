import math
import random

import pygame

import core

from pygame.math import Vector2




class Avatar:
    def __init__(self, largeur=1600, hauteur=900):
        self.nom = "ennemy1"
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon = 10
        self.rayonMAX = 150
        self.masse = 10
        self.speed = 10
        self.origine = Vector2(random.randint(0+self.rayon, largeur-self.rayon), random.randint(0+self.rayon, hauteur-self.rayon))
        self.force = Vector2(0, 0)
        self.vitesseMAX = 100
        self.vitesseMIN = 25
        self.accMAX = 0.5
        self.vivant = True


    def move(self, creep,joueur):

        for p in creep:
            if p.vivant:
                position = p.origine
        x = Vector2(position)
        v = Vector2((x - self.origine))
        u = v.normalize()
        if self.origine != x:
            vitesse = self.speed * u
            self.origine = self.origine + vitesse

        if self.origine.y + self.rayon > 900:
            self.origine = Vector2(self.origine.x, 900 - self.rayon)

        if self.origine.y - self.rayon < 0:
            self.origine = Vector2(self.origine.x, self.rayon)

        if self.origine.x + self.rayon > 1600:
            self.origine = Vector2(1600 - self.rayon, self.origine.y)

        if self.origine.x - self.rayon < 0:
            self.origine = Vector2(self.rayon, self.origine.y)

    def show(self, screen):
            pygame.draw.circle(screen, self.couleur,self.origine, self.rayon)
            core.Draw.text((0, 0, 0), self.nom, self.origine)

    def manger(self, creep):
        for p in creep:
            if p.origine.distance_to(self.origine) < self.rayon + p.rayon:
                if p.vivant:
                    if self.rayon < self.rayonMAX:
                        self.rayon += 0.5
                p.vivant = False

    def death(self):
        if core.memory("tempo") != 60:
            core.memory("tempo", core.memory("tempo") + 1)
        else:
            core.memory("tempo", 0)
            self.rayon = 10
            self.vivant = True
            self.origine = Vector2(random.randint(0 + self.rayon, core.WINDOW_SIZE[1] - self.rayon),
                                random.randint(0 + self.rayon, core.WINDOW_SIZE[0] - self.rayon))
