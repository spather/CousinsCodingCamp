# Lesson 08

## WIP - Just an outline for now

Exploding Asteroids!
  * New asteroid images
    * ASTEROID_HEIGHT constant
  * New frame counter
  * Exploding and frame properties on each asteroid
  * update_exploding_asteroids to run the animation
    * finding ideal frame rate of 14
  * When game over, still draw exploding asteroids
    * move update_exploding_asteroids call to before early bail out of update()
      but didn't draw exploding asteroids in draw()