WIDTH = 500
HEIGHT = 300

alien = Actor("alien")
alien.pos = 100, 56

def draw():
    screen.fill((0, 102, 255))
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.left = 0
