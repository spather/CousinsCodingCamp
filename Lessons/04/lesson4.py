# Write your code here :-)
from random import randint

WIDTH = 500
HEIGHT = 300

alien = Actor("alien")
alien.pos = 100, 56

def makeAsteroid(left, top):
    asteroid = Actor("asteroid")
    asteroid.left = left
    asteroid.top = top
    return asteroid

asteroids = [
    makeAsteroid(WIDTH, randint(0, HEIGHT-100)),
    makeAsteroid(WIDTH+120, randint(0, HEIGHT-100)),
    makeAsteroid(WIDTH+240, randint(0, HEIGHT-100))
]

def draw():
    screen.fill((0, 102, 255))
    alien.draw()
    for asteroid in asteroids:
        asteroid.draw()

def update():
    for asteroid in asteroids:
        asteroid.left -= 2
        if asteroid.right < 0:
            asteroid.left = WIDTH
            asteroid.top = randint(0, HEIGHT-100)
        if alien.colliderect(asteroid):
            alien.image = "alien_hurt"
            # sounds.eep.play()
            clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = "alien"

def on_key_down(key):
    if key == keys.DOWN:
        alien.top += 10
    elif key == keys.UP:
        alien.top -= 10
    if alien.top < 0:
        alien.top = 0;
    if alien.bottom > HEIGHT:
        alien.bottom = HEIGHT
