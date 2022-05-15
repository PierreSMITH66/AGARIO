import random

import avatar
import core
import pygame
from pygame.math import Vector2

import creep
import ennemy
import screen


def setup():

    print("Setup START--------------")
    screen.Screen()
    core.memory("nbrcreep", 100)
    core.memory("listcreep", [])
    core.memory("joueur",[])
    core.memory("ennemy", [])
    core.memory("tempo", 0)
    core.memory("tempoc",0)
    core.memory("distancecreep", [])
    core.memory("nearcreep",[])

    for i in range(0, core.memory("nbrcreep")):
        core.memory("listcreep").append(creep.Creep(core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))
    core.memory("joueur").append(avatar.Avatar())
    core.memory("ennemy").append(ennemy.Avatar())
    print("Setup END----------------")


def run():
    core.cleanScreen()
    for c in core.memory("joueur"):
        if c.vivant:
            c.show(core.screen)
            c.manger(core.memory("listcreep"))
            c.manger(core.memory("ennemy"))
        else:
            c.death

        if core.getMouseRightClick():
            c.move()

    for c in core.memory("listcreep"):
        if c.vivant:
            c.show(core.screen)
        else:
            c.death()

    for c in core.memory("ennemy"):
        if c.vivant:
            c.show(core.screen)
            c.manger(core.memory("listcreep"))
            c.manger(core.memory("joueur"))
            c.move(core.memory("listcreep"),core.memory("joueur"))
        else:
            c.death()





core.main(setup, run)




