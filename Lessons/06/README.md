# Lesson 06

## WIP - Just an outline for now

In the last lesson, we introduced the concept of lives into the game, and made the game end when the player loses all their lives. But, unless they're counting themselves, the player has no way to know how many lives they have at any given moment. In this lesson, we'll create a status bar at the top of the game window, and in it, we'll draw a series of hearts showing how many lives the player has left.

[Add link to initial code - should just be final code of the last lesson]

# Preparing for the status bar

First, make the window bigger:

<pre>
WIDTH = 500
<b>HEIGHT = </b><del>300</del><b>500</b>
</pre>

Currently, the whole window is the play area, so our code assumes it starts at (0, 0) and ends at (WIDTH, HEIGHT). We've built this assumption in all over the place, e.g.:

<pre>
asteroids = [
    makeAsteroid(<b>WIDTH</b>, randint(0, <b>HEIGHT</b>-100)),
    makeAsteroid(<b>WIDTH</b>+120, randint(0, <b>HEIGHT</b>-100)),
    makeAsteroid(<b>WIDTH</b>+240, randint(0, <b>HEIGHT</b>-100))
]
...
def update():
    ...
    if alien.top < <b>0</b>:
        alien.top = <b>0</b>;
    if alien.bottom > <b>HEIGHT</b>:
        alien.bottom = <b>HEIGHT</b>
</pre>

The status bar we're going to introduce at the top is going to consume part of the window, so we can't assume the play area takes up the whole thing. Let's explicitly define the play area bounds and clean the code up to reference this. Then, we can easily change it.

<pre>
...
WIDTH = 500
HEIGHT = 500

<b>play_area = Rect((0, 0), (WIDTH, HEIGHT))</b>

alien = Actor("alien")
...
</pre>

[Explain what Rect is and why it's important to do this, even if the bounds are currently still (0, 0) and (WIDTH, HEIGHT).]

Now let's fix up all the code.

Asteroid creation:

```python
asteroids = [
    makeAsteroid(play_area.right, randint(play_area.top, play_area.bottom-100)),
    makeAsteroid(play_area.right+120, randint(play_area.top, play_area.bottom-100)),
    makeAsteroid(play_area.right+240, randint(play_area.top, play_area.bottom-100))
]
```
Bounds checking in update():

<pre>
def update():
    global lives
    global alien_can_hurt

    alien.top += alien_y_speed
    <b>if alien.top < play_area.top:
        alien.top = play_area.top
    if alien.bottom > play_area.bottom:
        alien.bottom = play_area.bottom</b>

    if lives <= 0:
        return

    for asteroid in asteroids:
        asteroid.left -= 2
        <b>if asteroid.right < play_area.left:
            asteroid.left = play_area.right
            asteroid.top = randint(play_area.top, play_area.bottom-100)</b>
        if alien.colliderect(asteroid) and alien_can_hurt:
        ...
</pre>

# Implementing the status bar

Now let's create a rect for the status bar, and adjust the `play_area` rect accordingly:

<pre>
WIDTH = 500
HEIGHT = 500

<b>status_bar = Rect((0, 0), (WIDTH, 20))</b>
play_area = Rect((0, <b>status_bar.bottom</b>), (WIDTH, HEIGHT<b>-status_bar.height</b>))
</pre>

[Note that this is all we have to change to adjust the play area, because we defined everything else in terms of the play area rect]

Draw it:
<pre>
def draw():
    screen.fill((0, 102, 255))
    alien.draw()

    <b># Draw status bar
    screen.draw.filled_rect(status_bar, (0, 20, 150))</b>

    if lives <= 0:
    ...
</pre>

Note that we want to draw it before the `if lives <= 0` check because we want the status bar to show even in the game over state

[Screenshot showing blue bar here]

# Drawing the hearts for lives

Explain about heart icon (<img alt="heart icon" src="heart-icon.png">) and moving it to the images folder.

Need a diagram here explaining heart placement
<pre>
def draw():
    ...

    for asteroid in asteroids:
        asteroid.draw()

    <b># Draw lives hearts
    hearts_drawn = 0
    heart_left = WIDTH - 20
    while (hearts_drawn < lives):
        screen.blit("heart-icon", (heart_left, 0))
        hearts_drawn += 1
        heart_left -= 20</b>
</pre>
