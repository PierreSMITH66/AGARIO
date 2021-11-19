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

    for i in range(0, core.memory("nbrcreep")):
        core.memory("listcreep").append(creep.Creep(core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))


    print("Setup END----------------")



def run():
    core.cleanScreen()
    avatar.show()

    for c in core.memory("listcreep"):
        c.show(core.screen)


    if core.getMouseLeftClick():
        avatar.move()
        avatar.show()

core.main(setup, run)




