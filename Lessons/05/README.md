# Lesson 05

In Lesson 5, we made changes to the keyboard controls to make it easier to move the alien around. We also added the concept of lives to the game: now, after the alien is hit three times, it's Game Over!

Here's everything we learned to do:
* Use global variables
* Respond to both key down and key up events, to enable movement when the player holds down a key.
* Keep track of the number of lives the alien has, which was trickier than we expected!

# Improving Keyboard Controls
In Lesson 3, we implemented the code that let the player move the alien up and down with the arrow keys. Our code detected when the up or down key was pressed, and then moved the alien up or down by 10 pixels each time. That code looks like this:

```
def on_key_down(key):
    if key == keys.DOWN:
        alien.top += 10
    elif key == keys.UP:
        alien.top -= 10
    ...
```

When playing, you may have tried holding the arrow keys down, hoping the alien would keep moving as long as you kept the key pressed down. But sadly, this doesn't work. That's because the code we wrote responded to the arrow keys being pressed *down* and each downward press of the key resulted in one 10-pixel movement. If you held the key down, you made just one downward press, so our code made one 10-pixel movement.

What we implemented works, but doesn't feel great when we play the game. We end up having to mash the arrow keys multiple to times to get the alien to move fast and the movement looks and feels a little jumpy. Let's see if we can do better.

To begin, let's first describe the behavior we want: We'd like the player to be able to press and hold the up key or down key, and have the alien keep moving smoothly in the appropriate direction, as long as the key is pressed.


## A New Mental Model

To implement this, we have to change how we think about the alien's movement. The way we have it currently implemented, we only move the alien (by changing `alien.top`) when a key is pressed down. What actually happens is something like this sequence of events:


* `update()` changes the asteroids' positions by setting `asteroid.top` and `asteroid.left`
* `draw()` draws the alien and asteroids at their current positions
* `update()` changes the asteroids' positions by setting `asteroid.top` and `asteroid.left`
* `draw()` draws the alien and asteroids at their current positions

... and so on, 60 times per second ... then an up- or down-arrow key press happens:

* **`on_key_down()` changes the alien's position by setting `alien.top`**
* `update()` changes the asteroids' positions by setting `asteroid.top` and `asteroid.left`
* `draw()` draws the alien and asteroids at their current positions

... and so on, 60 times per second

Instead, what if we moved the alien, by changing `alien.top`, on *every frame* (every time `update()` is called, which happens 60 times per second)? This would result in the alien moving smoothly, like the asteroids do.

But, the asteroids just move autonomously, all the time, and we want the alien's movement to be in the player's control. Specifically, we want the alien's amount and direction of movement to depend on the keys pressed. So we can't just adjust the alien's position by a set number of pixels in each `update()` call, like we do for the asteroids.

Let's break down what we want to happen in the different cases:
* If no key is pressed, we don't want the alien to move; `update()` should not change `alien.top`.
* If the down arrow key is pressed, we want the alien to move down; `update()` should *add* to `alien.top` - make the value bigger - because bigger values are further down along the y-axis.
* If the up arrow key is pressed, we want the alien to move down; `update()` should *subtract* from `alien.top` - make the value smaller - because smaller values are further up along the y-axis.

<p align="center">
  <img alt="Diagram showing the axes and the directions in which values get bigger" src="assets/axes.png" />
</p>

These statements express what should happen in the way humans normally talk to each other. But we can also express express them in a more Computer Science-like way, that makes it easier to translate them into code:

| Case | Human Way | Computer Science Way |
|------|-----------|----------------------|
| If no key is pressed, `update()` should | not change `alien.top` | add `0` to `alien.top` |
| If down key is pressed, `update()` should | add to `alien.top` | add a positive number to `alien.top` |
| If no key is pressed, `update()` should | subtract from `alien.top` | add a negative number to `alien.top` |

Go through the lines in this table one by one, and make sure you understand why the "Human Way" and "Computer Science Way" descriptions are really saying the same thing.

Looking at the "Computer Science Way" column, we see that in every case, we just add something to `alien.top`. The only difference between the cases is what value we add (0, a positive number, or a negative number). In code, this means:

* We can create a variable to hold the value we want added to `alien.top`.
* The code that detects key presses can change the value of this variable.
* `update()` can just add the value in this variable to `alien.top` in each frame.


## Implementing the New Model

OK, that was a lot of explaining! Let's get back into some code!

To begin, let's make sure we're starting from the right place. Your game code should look like this:

```python
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
```

This code is the end state from the previous lesson. If your code doesn't look like this, just create a new file for this lesson, and copy the code above into it and you'll be ready to go.

### New Alien Movement Code

First, let's create the variable we're going to use to store the value that we'll add to `alien.top` in each frame. We're going to call this variable `alien_y_speed` because it represents the speed the alien moves in the y direction. Create this variable and set it to 0, near the top of the program, just after you create the alien. The snippet below shows where the new line (bolded) should appear:

<pre>
WIDTH = 500
HEIGHT = 300

alien = Actor("alien")
alien.pos = 100, 56

<b>alien_y_speed = 0</b>

def makeAsteroid(left, top):
...
</pre>

Next, let's change `update()` to adjust `alien.top` using this variable:

<pre>
def update():
    <b>alien.top += alien_y_speed</b>

    for asteroid in asteroids:
    ...
</pre>

We're using `+=` to say "take what's in `alien.top` and add what's in `alien_y_speed`". If we just add to `alien.top`, we might actually move the alien off the top or bottom of the screen (because `alien.top` might end up being less than 0 or bigger than `HEIGHT`).

We had this problem when we first introduced keyboard movement in Lesson 3, and fixed it in an exercise. The code that fixes it is currently in our `on_key_down` handler:

<pre>
def on_key_down(key):
    if key == keys.DOWN:
        alien.top += 10
    elif key == keys.UP:
        alien.top -= 10
    <b>if alien.top < 0:
        alien.top = 0;
    if alien.bottom > HEIGHT:
        alien.bottom = HEIGHT</b>
</pre>

It checks whether `alien.top` has become less than `0` (and adjusts it to `0`, if so) or greater than `HEIGHT` (and adjusts it to `HEIGHT` if so). Since we are now performing adjustments to `alien.top` in `update()`, we need to move this code (shown in bold above) there. Remove it from `on_key_down()` and add it to `update()` just after the line we just added to change `alien.top`:

<pre>
def update():
    alien.top += alien_y_speed
    <b>if alien.top < 0:
        alien.top = 0;
    if alien.bottom > HEIGHT:
        alien.bottom = HEIGHT</b>

    for asteroid in asteroids:

...

def on_key_down(key):
    if key == keys.DOWN:
        alien.top += 10
    elif key == keys.UP:
        alien.top -= 10
</pre>

Note: `on_key_down()` currently still changes `alien.top` so you might be worried about removing this code from there, but we're about to change `on_key_down()` to not change `alien.top` shortly.


OK, so now we have our variable that controls how much we adjust `alien.top` in each frame, and the code in `update()` that performs the adjustment, along with the check to make sure the alien doesn't move out of the frame. Next, we need to write the code to adjust the value stored in `alien_y_speed` depending on key presses.

### Handling Key Down Events
We'll start with the downward key presses, which we handle in `on_key_down()`. Change `on_key_down` to read as follows:

```python
def on_key_down(key):
    global alien_y_speed
    if key == keys.DOWN:
        alien_y_speed = 2
    elif key == keys.UP:
        alien_y_speed = -2
```

Ignore the `global alien_y_speed` for a moment - I'll come back to it shortly.

Remember that `on_key_down()` is called whenever a key is pressed *down*. The parameter, `key`, gets a value that indicates which key was pressed down. We can compare this value against variables in the `keys` object to determine which key was pressed. Now, when the down key is pressed, we set `alien_y_speed` to `2` and when the up key is pressed, we set `alien_y_speed` to `-2`. Combined with the code we just wrote above, this will cause `update()` to add `2` or `-2` to `alien.top` each frame, moving the alien down or up, depending on which key was pressed.

Now, back to that `global alien_y_speed` line; to understand this, you need to understand a new concept:

### Global and Local Variables
`alien_y_speed` is what's known as a **global variable**. We created it outside of any function, so it belongs to the whole program. To understand global variables, it helps to first understand the opposite.

When you create a variable inside a function, that variable only exists for the code inside the function. We call such a variable a **local variable**. If you tried to access a local variable outside the function that created it, you'd get an error. Here's a silly example that illustrates this (don't add this to your game code - I'm just using it here to explain the concept of global and local variables):

```python
def myFunction():
    name = "Sammy"
    print("Inside myFunction, name is: " + name) # This works

myFunction()
print("Outside myFunction, name is: " + name) # NameError: name 'name' is not defined
```

In `myFunction()` we create a variable, `name`, give it a value and then print its value. This works. But if we try to print the variable's value outside `myFunction()`, we get an error: Python doesn't know about a variable called `name` outside `myFunction()`, because it's *local* to `myFunction()`.

This might seem a little surprising or strange, but it's actually a really good thing that variables created inside functions are local, by default. It makes a lot of things simpler: you don't have to worry that another function might have already created a variable with the same name, or that some code outside your function might change what's in your variables in a way you don't expect. It also means that each time your function runs, the local variables are created again, fresh. So you don't have to think about what happens to the values in those variables across function calls.

Global variables, on the other hand, can be accessed in many different functions and even in code that isn't in any function. Global variables keep whatever value they hold across function calls. So if one function puts a value into a global variable, when another function reads from the variable, it will see that value.

Earlier, we said that `alien_y_speed` is a global variable. Why does it have to be global? Because it contains information that we need in different functions: we set it in `on_key_down()` and we read its value in `update()`.

In our `on_key_down()` function, look at the line `alien_y_speed = 2`. That line could mean two different things: "create a local variable called `alien_y_speed` and assign it the value `2`" or "put `2` in the global variable `alien_y_speed`". How would the Python interpreter know which one we mean? The answer is the line `global alien_y_speed` at the top of the function. That line tells the Python interpreter that we'll be referencing a global variable called `alien_y_speed` inside this function.

Notice that in `update()`, we didn't need the `global` keyword to access `alien_y_speed`. That's because we're only reading a value from the variable, not putting a new value into it. In Python, any variable that you read from in a function is assumed to be global, unless you created it inside the function. In contrast, any variable you create inside a function is assumed to be local, unless you use the `global` keyword to mark it as global. The rationale for this is explained in [the Python documentation](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python).

Here's a silly example that shows the behavior of global variables (again, don't put this in your game code but just read and think about what it does):

```python
name = "Sammy" # name is created outside of any function, so it's global
print(name) # code outside of a function can use name

def greet():
    print("Hello " + name) # Can access name inside this function

def changeName():
    global name # Tell Python that name refers to a global variable
    name = "Khiyal" # Set name to a new value

greet() # Prints "Hello Sammy"
changeName() # Puts "Khiyal" into name
greet() # Now prints "Hello Khiyal"
```

### Handling Key Up Events
So far, we've made the changes to move the alien based on the value in the global variable `alien_y_speed` and we set `alien_y_speed` to the values needed to move the alien up or down, when the up or down arrow key is pressed down. But if you run the game now, you'll notice that once the alien starts moving, it never stops, even if you release the key. Take a moment and think about why that's happening.

The answer is that we don't have any code that sets `alien_y_speed` back to zero when the key is released. Let's add that now. When a key is pressed down, `on_key_down()` is called. As you might guess, `on_key_up()` is called when a key is released. `on_key_up()`, just like `on_key_down`, takes a `key` parameter which you can use to tell which key was released.

Add this `on_key_up()` function to your code:

```python
def on_key_up(key):
    global alien_y_speed
    if key == keys.DOWN:
        alien_y_speed = 0
    elif key == keys.UP:
        alien_y_speed = 0
```

This implementation should be fairly straightforward to understand. First, we tell Python that we'll be referencing the global variable `alien_y_speed`. Then, if the key released is either the up or down arrow, we set alien_y_speed to zero.

Now, when you run the code, you should be able to move the alien up or down continuously by holding down the appropriate key. When you release the key, the alien stops moving.



