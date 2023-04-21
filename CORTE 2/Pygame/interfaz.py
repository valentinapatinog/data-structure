import pygame as py
py.init()

display = py.display.set_mode((800, 500))
py.display.set_caption("Superheroes")

Bandera = True
Clock = py.time.Clock()

while Bandera:
    Clock.tick(30)
    event_list = py.event.get()
    
    for event in event_list:
        if event.type == py.QUIT:
            Bandera = False

    py.display.flip()