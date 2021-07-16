from random import randint

WIDTH = 500
HEIGHT = 500

status_bar = Rect((0, 0), (WIDTH, 20))
play_area = Rect((0, status_bar.bottom), (WIDTH, HEIGHT-status_bar.height))

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
    makeAsteroid(play_area.right, randint(play_area.top, play_area.bottom-100)),
    makeAsteroid(play_area.right+120, randint(play_area.top, play_area.bottom-100)),
    makeAsteroid(play_area.right+240, randint(play_area.top, play_area.bottom-100))
]

def draw():
    screen.fill((0, 102, 255))
    alien.draw()

    # Draw status bar
    screen.draw.filled_rect(status_bar, (0, 20, 150))

    if lives <= 0:
        screen.draw.text("Game Over", center=(250, 150), fontsize=60)
        return

    for asteroid in asteroids:
        asteroid.draw()

    # Draw lives hearts
    hearts_drawn = 0
    heart_left = status_bar.right - 20
    while (hearts_drawn < lives):
        screen.blit("heart-icon", (heart_left, 0))
        hearts_drawn += 1
        heart_left -= 20

def update():
    global lives
    global alien_can_hurt

    alien.top += alien_y_speed
    if alien.top < play_area.top:
        alien.top = play_area.top
    if alien.bottom > play_area.bottom:
        alien.bottom = play_area.bottom

    if lives <= 0:
        return

    for asteroid in asteroids:
        asteroid.left -= 2
        if asteroid.right < play_area.left:
            asteroid.left = play_area.right
            asteroid.top = randint(play_area.top, play_area.bottom-100)
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
