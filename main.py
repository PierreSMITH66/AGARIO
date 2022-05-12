import random

import avatar
import core
import pygame
from pygame.math import Vector2

import creep
import ennemy
import screen
import time

def setup():

    print("Setup START--------------")
    screen.Screen()
    core.memory("nbrcreep", 100)
    core.memory("listcreep", [])
    core.memory("joueur",[])
    core.memory("ennemy", [])
    core.memory("tempo", 0)


    for i in range(0, core.memory("nbrcreep")):
        core.memory("listcreep").append(creep.Creep(core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))
    core.memory("joueur").append(avatar.Avatar())
    core.memory("ennemy").append(ennemy.Avatar())
    print("Setup END----------------")


def run():
    core.cleanScreen()
    for c in core.memory("joueur"):
        c.show(core.screen)
        c.manger(core.memory("listcreep"))
        c.manger(core.memory("ennemy"))

        if core.getMouseRightClick():
            c.move()

    for c in core.memory("listcreep"):
        c.show(core.screen)

    for c in core.memory("ennemy"):
        if c.vivant:
            c.show(core.screen)
            c.manger(core.memory("listcreep"))
            c.move(core.memory("listcreep"),core.memory("joueur"))
        else:
            if  core.memory("tempo") != 60 :
                core.memory("tempo",core.memory("tempo") + 1)
            else:
                core.memory("tempo", 0)
                c.rayon = 10
                c.vivant = True
                c.origine = Vector2(random.randint(0 + c.rayon, core.WINDOW_SIZE[1] - c.rayon),random.randint(0 + c.rayon, core.WINDOW_SIZE[0] - c.rayon))



core.main(setup, run)




