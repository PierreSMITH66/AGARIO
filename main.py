import random

import avatar
import core
import pygame
from pygame.math import Vector2

import creep
import screen


def setup():

    print("Setup START--------------")
    screen.Screen()
    core.memory("nbrcreep", 100)
    core.memory("listcreep", [])
    core.memory("joueur",[])

    for i in range(0, core.memory("nbrcreep")):
        core.memory("listcreep").append(creep.Creep(core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))
    core.memory("joueur").append(avatar.Avatar())

    print("Setup END----------------")


def run():
    core.cleanScreen()

    for c in core.memory("joueur"):
        c.show(core.screen)
        c.manger(core.memory("listcreep"))

        if core.getMouseRightClick():
            avatar.Avatar.move(c)

    for c in core.memory("listcreep"):
        c.show(core.screen)





core.main(setup, run)




