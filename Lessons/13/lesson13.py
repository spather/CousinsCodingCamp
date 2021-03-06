from enum import Enum
from random import randint

WIDTH = 500
HEIGHT = 500

ASTEROID_HEIGHT = 50
ASTEROID_EXPLOSION_MAX_FRAME = 6

BackgroundType = Enum("BackgroundType", [
    "COSMIC",
    "JUMPING_STAR",
    "NEPTUNE",
    "RADAR",
    "GOOD_JOB"
])

GameState = Enum("GameState", [
    "READY",
    "PLAYING",
    "GAME_OVER",
])

status_bar = Rect((0, 0), (WIDTH, 20))
play_area = Rect((0, status_bar.bottom), (WIDTH, HEIGHT-status_bar.height))

def reset_game():
    global game_state
    global alien
    global alien_y_speed
    global lives
    global alien_can_hurt
    global score
    global frame
    global level
    global paused
    global sounds_enabled
    global background_type
    global background_change_frame
    global asteroids

    game_state = GameState.READY

    alien = Actor("alien")
    alien.pos = 100, 80

    alien_y_speed = 0
    lives = 3
    alien_can_hurt = True
    score = 0
    frame = 0
    level = 0
    paused = False
    # Sound flag is off for now
    sounds_enabled = False
    background_type = BackgroundType.COSMIC
    background_change_frame = 0

    asteroids = [
        makeAsteroid(play_area.right, randint(play_area.top, play_area.bottom-ASTEROID_HEIGHT)),
        makeAsteroid(play_area.right+120, randint(play_area.top, play_area.bottom-ASTEROID_HEIGHT)),
        makeAsteroid(play_area.right+240, randint(play_area.top, play_area.bottom-ASTEROID_HEIGHT))
    ]

def play_sound(name):
    if not sounds_enabled:
        return
    sound = getattr(sounds, name)
    sound.play()

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

def get_background_type():
    if level == 0:
        return BackgroundType.COSMIC
    elif level == 1:
        return BackgroundType.JUMPING_STAR
    elif level == 2:
        return BackgroundType.NEPTUNE
    elif level == 3:
        return BackgroundType.RADAR
    else:
        return BackgroundType.GOOD_JOB

def get_background_filename():
    if background_type == BackgroundType.COSMIC:
        return "cosmic-background"
    elif background_type == BackgroundType.JUMPING_STAR:
        return "jumping-star-{}".format(int(((frame - background_change_frame) % 66) / 6))
    elif background_type == BackgroundType.NEPTUNE:
        return "neptune-background"
    elif background_type == BackgroundType.RADAR:
        return "radar-{}".format(int(((frame - background_change_frame) % 84) / 6))
    elif background_type == BackgroundType.GOOD_JOB:
        return "good-job-background"

def draw_background():
    global background_type
    global background_change_frame

    if game_state == GameState.READY:
        filename = "start-screen"
    elif game_state == GameState.GAME_OVER:
        filename = "game-over"
    elif game_state == GameState.PLAYING:
        new_background_type = get_background_type()

        if new_background_type != background_type:
            background_type = new_background_type
            background_change_frame = frame

        filename = get_background_filename()

    screen.blit(filename, (0, 0))

def draw():
    draw_background()

    if game_state == GameState.READY:
        return

    alien.draw()

    # Draw status bar
    screen.draw.filled_rect(status_bar, (0, 20, 150))

    # Draw score
    screen.draw.text(str(score), topleft=(status_bar.left+10, status_bar.top+5), fontsize=20)

    # Draw Paused Message or Level
    if paused:
        screen.draw.text("Paused", midtop=(status_bar.width/2, 5), fontsize=20)
    else:
        screen.draw.text("Level {}".format(level+1), midtop=(status_bar.width/2, 5), fontsize=20)

    if game_state == GameState.GAME_OVER:
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
    global level
    global game_state

    if paused:
        return

    frame += 1

    if game_state == GameState.READY:
        return

    alien.top += alien_y_speed
    if alien.top < play_area.top:
        alien.top = play_area.top
    if alien.bottom > play_area.bottom:
        alien.bottom = play_area.bottom

    update_asteroid_explosions(frame)

    if game_state == GameState.GAME_OVER:
        return

    for asteroid in asteroids:
        update_asteroid(asteroid, level)
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
            play_sound("eep")
            if lives > 0:
                clock.schedule_unique(set_alien_normal, 2.0)

        if asteroid.right < alien.left:
            score += asteroid.points
            if asteroid.points > 0:
                play_sound("points")
            asteroid.points = 0

    # Update level
    newlevel = int(score / 100)
    if newlevel != level:
        level = newlevel
        play_sound("level_up")

    # Update game state
    if lives <= 0:
        game_state = GameState.GAME_OVER

def update_asteroid(asteroid, level):
    asteroid.left -= 2 + level

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

    if game_state == GameState.READY:
        return

    if key == keys.DOWN:
        alien_y_speed = 2
    elif key == keys.UP:
        alien_y_speed = -2

def on_key_up(key):
    global alien_y_speed
    global paused
    global game_state

    if game_state == GameState.READY:
        if key == keys.SPACE:
            game_state = GameState.PLAYING
            return

    if game_state == GameState.PLAYING:
        if key == keys.P:
            paused = not paused

    if game_state == GameState.PLAYING or game_state == GameState.GAME_OVER:
        if key == keys.DOWN:
            alien_y_speed = 0
        elif key == keys.UP:
            alien_y_speed = 0

    if game_state == GameState.GAME_OVER:
        if key == keys.R:
            reset_game()

reset_game()
