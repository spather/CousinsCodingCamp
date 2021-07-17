from random import randint

WIDTH = 500
HEIGHT = 500

ASTEROID_HEIGHT = 50
ASTEROID_EXPLOSION_MAX_FRAME = 6

status_bar = Rect((0, 0), (WIDTH, 20))
play_area = Rect((0, status_bar.bottom), (WIDTH, HEIGHT-status_bar.height))

alien = Actor("alien")
alien.pos = 100, 56

alien_y_speed = 0
lives = 3
alien_can_hurt = True
score = 0
frame = 0
paused = False

def makeAsteroid(left, top):
    asteroid = Actor("asteroid")
    reset_asteroid(asteroid, left, top)
    return asteroid

def reset_asteroid(asteroid, left, top):
    asteroid.left = left
    asteroid.top = top
    asteroid.points = 10
    asteroid.exploding = False
    asteroid.frame = 0
    asteroid.image = "asteroid"

asteroids = [
    makeAsteroid(play_area.right, randint(play_area.top, play_area.bottom-ASTEROID_HEIGHT)),
    makeAsteroid(play_area.right+120, randint(play_area.top, play_area.bottom-ASTEROID_HEIGHT)),
    makeAsteroid(play_area.right+240, randint(play_area.top, play_area.bottom-ASTEROID_HEIGHT))
]

def draw():
    screen.blit("cosmic-background", (0, 0))
    alien.draw()

    # Draw status bar
    screen.draw.filled_rect(status_bar, (0, 20, 150))

    # Draw score
    screen.draw.text(str(score), topleft=(status_bar.left+10, status_bar.top+5), fontsize=20)

    # Draw Paused Message
    if paused:
        screen.draw.text("Paused", midtop=(status_bar.width/2, 5), fontsize=20)

    if lives <= 0:
        screen.draw.text("Game Over", center=(250, 150), fontsize=60)
        for asteroid in asteroids:
            if asteroid.exploding:
                asteroid.draw()
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
    global score
    global frame

    if paused:
        return

    frame += 1

    alien.top += alien_y_speed
    if alien.top < play_area.top:
        alien.top = play_area.top
    if alien.bottom > play_area.bottom:
        alien.bottom = play_area.bottom

    update_asteroid_explosions(frame)

    if lives <= 0:
        return

    for asteroid in asteroids:
        asteroid.left -= 2
        if asteroid.right < play_area.left:
            reset_asteroid(
                asteroid,
                play_area.right,
                randint(play_area.top, play_area.bottom-ASTEROID_HEIGHT))

        if alien.colliderect(asteroid) and alien_can_hurt:
            asteroid.points = 0
            asteroid.exploding = True
            alien.image = "alien_hurt"
            lives -= 1
            print("Decreased lives to: " + str(lives))
            alien_can_hurt = False
            # sounds.eep.play()
            if lives > 0:
                clock.schedule_unique(set_alien_normal, 2.0)

        if asteroid.right < alien.left:
            score += asteroid.points
            asteroid.points = 0

def update_asteroid_explosions(frame):
    for asteroid in asteroids:
        if asteroid.exploding and frame % 14 == 0:
            asteroid.image = "asteroid{}".format(asteroid.frame)
            asteroid.frame += 1
            if asteroid.frame > ASTEROID_EXPLOSION_MAX_FRAME:
                asteroid.exploding = False
                asteroid.frame = 0
                asteroid.image = "asteroid"

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
    global paused
    if key == keys.DOWN:
        alien_y_speed = 0
    elif key == keys.UP:
        alien_y_speed = 0
    elif key == keys.P:
        paused = not paused
