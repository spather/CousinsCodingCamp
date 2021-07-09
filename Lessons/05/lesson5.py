from random import randint

WIDTH = 500
HEIGHT = 300

alien = Actor("alien")
alien.pos = 100, 56

alien_y_speed = 0
lives = 3
alien_can_hurt = True

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

    if lives <= 0:
        screen.draw.text("Game Over", center=(250, 150), fontsize=60)
        return

    for asteroid in asteroids:
        asteroid.draw()

def update():
    global lives
    global alien_can_hurt

    alien.top += alien_y_speed
    if alien.top < 0:
        alien.top = 0;
    if alien.bottom > HEIGHT:
        alien.bottom = HEIGHT

    if lives <= 0:
        return

    for asteroid in asteroids:
        asteroid.left -= 2
        if asteroid.right < 0:
            asteroid.left = WIDTH
            asteroid.top = randint(0, HEIGHT-100)
        if alien.colliderect(asteroid) and alien_can_hurt:
            alien.image = "alien_hurt"
            lives -= 1
            print("Decreased lives to: " + str(lives))
            alien_can_hurt = False
            # sounds.eep.play()
            clock.schedule_unique(set_alien_normal, 2.0)

def set_alien_normal():
    global alien_can_hurt
    alien_can_hurt = True
    alien.image = "alien"

def on_key_down(key):
    global alien_y_speed
    if key == keys.DOWN:
        alien_y_speed = 2
    elif key == keys.UP:
        alien_y_speed = -2

def on_key_up(key):
    global alien_y_speed
    if key == keys.DOWN:
        alien_y_speed = 0
    elif key == keys.UP:
        alien_y_speed = 0
