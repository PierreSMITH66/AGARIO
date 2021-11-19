'''core.memory("origine", Vector2(core.WINDOW_SIZE[0]/2, core.WINDOW_SIZE[1]/2))
        core.memory("rayonducercle", 400)
        core.memory("couleurducercle", (255, 0, 0))

        core.memory("vitesse", Vector2(0, 0))
        core.memory("acceleration", Vector2(0, 0))
        core.memory("maxacc", 0.5)

        core.memory("F", (0, 0))

        core.memory("k", 0.001)
        core.memory("l0", 10)


    if core.getMouseLeftClick():
        x = Vector2(core.getMouseLeftClick())
        v = Vector2((x - core.memory("origine")))
        u = v.normalize()
        #l = sqrt(((x.x-core.memory("origine").x)**2)+((x.y-core.memory("origine").y)**2))
        l = v.length()
        fr = Vector2(core.memory("k")*(l-core.memory("l0"))*u)
        core.memory("F",fr)

    core.memory("vitesse",core.memory("vitesse")+core.memory("F"))
    core.memory("F", (0, 0))

    core.memory("origine", core.memory("origine") + core.memory("vitesse"))

    if core.memory("origine").y + core.memory("rayonducercle") > core.WINDOW_SIZE[1] :
        core.memory("origine", Vector2(core.memory("origine").x, core.WINDOW_SIZE[1]-core.memory("rayonducercle")))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    if core.memory("origine").y - core.memory("rayonducercle") < 0 :
        core.memory("origine", Vector2(core.memory("origine").x,core.memory("rayonducercle")))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    if core.memory("origine").x + core.memory("rayonducercle") > core.WINDOW_SIZE[0] :
        core.memory("origine", Vector2(core.WINDOW_SIZE[1]-core.memory("rayonducercle"),core.memory("origine").y))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    if core.memory("origine").x - core.memory("rayonducercle") < 0 :
        core.memory("origine", Vector2(core.memory("rayonducercle"),core.memory("origine").y))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


    pygame.draw.circle(core.screen, core.memory("couleurducercle"), [int(core.memory("origine").x),int(core.memory("origine").y)], core.memory("rayonducercle"))'''
