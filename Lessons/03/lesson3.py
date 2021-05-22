WIDTH = 500
HEIGHT = 300

alien = Actor("alien")
alien.pos = 100, 56

asteroid = Actor("asteroid")
asteroid.left = WIDTH
asteroid.top = 50

def draw():
    screen.fill((0, 102, 255))
    alien.draw()
    asteroid.draw()

def update():
    asteroid.left -= 2
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

