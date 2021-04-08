# Lesson 02

In Lesson 2, as promised, we finally started doing some actual game programming. But first, we had to learn about one more fundamental concept: functions.

After covering the basics of functions we created a simple program utilizing [PyGame Zero](https://pygame-zero.readthedocs.io/en/stable/introduction.html). We learned how to:

* Create a window of a specific width and height
* Fill the window with a background color, represented as RGB values
* Draw a sprite on the screen
* Make the sprite move across the screen

Some notes on these topics follow.

# Functions

When coding, we sometimes find ourselves needing to write the same lines of code over and over again, because our program needs to do the same things more than once. When this happens, we can of course write the same lines many times (maybe using copy and paste to make it easier for ourselves) but there is a better way!

In Python, we can use a **function** to group several lines of code together into a unit we can easily re-use wherever we need it. In the last lesson, we wrote code to ask the user their name, store the answer in a variable, and then print a greeting, using the name they entered. That code looked like this:

```
name = input("What is your name? ")
print("Hello " + name)
```

Let's say that we needed to use this code more than once in our program. We could of course copy and paste these lines wherever we needed them. Or, we could group these lines into a function, as follows:

```
def greet():
    name = input("What is your name? ")
    print("Hello " + name)
```

The first line, `def greet()` tells Python we are creating a function named `greet()`. The `def` stands for "define" - all function definitions start with this keyword. Next goes the name of the function. Next comes open and close parentheses (`()`). Don't worry about this for now - I'll explain why it's there a little later. The line ends with a colon.

Do you remember what a colon used at the end of a line means? Or what's going to come next? If you said something like "a colon means that an indented block of code is coming next", you're right! The colon indicates, that the next indented block of code goes with this line.

The intended block of code is the same code we used before. By putting it beneath the function definition like this, we are telling Python that this function is made up of these lines of code.

Having defined the function, if we were to run our program, nothing happens. Why?

Well, we've defined our function, but we have not actually used it. In programming, when we want to use a function we say we are *calling* that function. Let's call our function now - add this line after the function definition:

```
greet()
```

We call the function by writing its name followed by open and close parentheses (again, don't worry about those - I'll explain them shortly). If you run the code now, you'll see that it prompts for a name and then prints "Hello " followed by whatever name you entered.

If you wanted to do a second greeting, you could just call the function again by adding another `greet()` line. OK, so you might be wondering why bother with this? Yes, we've been able to run the code again by just adding one more line instead of repeating two lines, but is that a big deal?

In real programs, functions can contain many lines of code, sometimes even hundreds of lines. If you needed to run those lines more than once, repeating them would make your program much longer than if you just called the function again.

Note: While it's normal for functions in real programs to have maybe 10, 20, or even 50 lines of code, it's actually not a good idea for a single function to grow too big (say 100 lines or more). This isn't something you need to worry about right now, but can you think of what you'd do to make a very long function shorter?

Besides making it easier to reuse lines of code, functions have another benefit. Let's say we wanted to change something about the way we do greetings. Maybe instead of saying "Hello " followed by your name, we wanted to say "Namaste ". If we'd copied & pasted the code lines that do the greeting many times, we'd have to change this message in every copy. But if instead we'd defined a function that does the greeting and used that every time we needed to do a greeting, then we could just change the message inside the function once and that change would apply to every place the function is called.

This actually leads us to our next topic...

## Function Parameters
Let's say we did want to use our greet() function in more than one place in our code but sometimes we wanted to ask "What is your name? " and other times we wanted to ask "What are you called? ". We could of course define a second function to do the second type of greeting:

```
def greet2():
    name = input("What are you called? ")
    print("Hello " + name)
```

But notice that this function's code is exactly the same as the first `greet()` function, except for the message passed to `input()`. Rather than define a second function, there's a way to change our original `greet()` function so that we can tell it what message we want it to print when we call it.

To do that, we can change the function to take a parameter, like this:

```
def greet(message):
    name = input(message)
    print("Hello " + name)
```

Now, within the parentheses after the function name `greet`, we have the word `message`. What is `message`? It's a **parameter**. Think of it like a variable you can use inside the function. When someone calls this function, they will have to give a value for this variable. Let's look at how we'd call this version of `greet()` which takes a parameter:

```
greet("What are you called? ")
```

Inside the parentheses we put a string. This becomes the value for the `message` parameter. Wherever the code inside the function references the value of `message`, they will get this value.

Why is this helpful? Now, if you wanted to greet in one time with the message "What is your name? " you would call the function with `greet("What is your name? ")` and if later in the same program you wanted to greet with "What are you called? ", you could call the same function and just pass a different parameter value: `greet("What are you called? ")`. No need for two functions or to copy/paste the code.

Note: You might hear another word, "argument", be used in relation to parameters. Some people use "argument" and "parameter" interchangeably but technically they have different meanings. Parameters are what you write in the function definition, `message` in our case. Arguments are the values you give when you call the function, "What is your name? " or "What are you called? " in our example.

Now I'll finally explain why the original definition of `greet()` had the empty close and open parenthesis after it (`()`). You might already have guessed why. The reason is that, in a function definition, the function name is always followed by a list of parameters, enclosed with parentheses. When there are no parameters at all, as was the case in our first version of `greet()`, there is nothing between the parentheses. But we still need the parentheses there: the empty parentheses tell the Python interpreter that the function has takes no parameters.

We've now seen a function that takes no parameters and a function that takes one parameter. Of course, functions can take more than one parameter. For example, if we wanted to change greet so that both the input prompt message and the greeting string are parameters, we could write it as follows:


```
def greet(message, greeting):
    name = input(message)
    print(greeting + name)
```

This version of `greet()` takes two parameters, both enclosed within parentheses after the function's name. Instead of printing the hard-coded string "Hello ", in the greeting, we now print whatever was passed via the `greeting` parameter. Here are some sample calls to this two-parameter function:

```
greet("What is your name? ", "Hello ")
greet("What are you called? ", "Namaste ")
```

In the function call, we list parameter values one after the other, separated by commas, within the parenthesis that follow the function name.

In Python, functions can take up to 255 parameters, but in practice, you'll typically see at most 10 or so parameters for each function. A function with many more parameters than that would usually be sign of poorly organized code.

## Return Values
So far, functions have just been a useful way to group lines of code we might want to re-use. We can send values into the function via parameters. But so far, we haven't seen how to get values out of the function. We'll learn about that now.

Let's say we want to write a function to find the square of a number. As you know from math class, the square of a number is just the number multiplied by itself. In Python, we write multiplication with the asterisk (`*`) symbol rather than the `x` notation that we normally use. So we can write a function that calculates the square of a given number like this:

```
def square(num):
    num * num
```

Here we're defining a function called `square()` that takes one parameter: the number you'd like to square. Inside, it just multiples the number by itself, which is how we calculate a square.

We could call this function like this: `square(2)`. We'd be calling `square()` with the value `2` for the parameter `num`. But that wouldn't be all that useful. Yes, calling the function would make the Python interpreter compute 2 x 2, but we wouldn't be able to get our hands on the answer. Likely we'd want to print the answer or use it in another calculation. But as written, our function, though it computes the answer, doesn't give the answer back to the code that called it.

To fix this, we use a **return statement**:

```
def square(num):
    return num * num
```

This is nearly the same function definition, except that we've added the keyword `return` before the `num * num`. Now, when we call the function, it gives us a value back and we can put that in a variable and use it later in the program. For example:

```
answer = square(2)
print(answer)
```

The line `answer = square(2)` creates a variable called answer and puts in that variable the value returned from the call to `square(2)`. You can imagine that `square(2)` is replaced by the value the function returns, so that line effectively reads `answer = 4`. Once the return value is in the variable `answer`, we can use it; here's we're just printing it.

## Nesting Function Calls
Sometimes, we need to call more than one function in a row, passing the return value from the first function into the next. There's a technique called **nesting** that gives us a compact way to do this. To see it in action, let's first define another function:

```
def triple(num):
    return num * 3
```

This `triple()` function takes whatever number you give it and multiples it by 3. That's the very definition of tripling! And, of course, it returns the answer.

Let's say we wanted to start with the number 2, square it, and then triple that. We could write that as follows:

```
answer = square(2)
answer = triple(answer)
print(answer)
```

The first line calls `square()` with `2`, and puts the value returned into the variable `answer`. After this line `answer` should have the value `4`.

Next, we have an interesting line: `answer = triple(answer)`. Notice that the variable `answer` appears on both sides of the ` = `.  What's going on here? We are calling the function `triple()` and passing the value of `answer` for its parameter. After the `square(2)` call, `answer` should contain `4`. So this is basically equivalent to `triple(4)`. And the `answer =` part before the call to `triple()` means that whatever value is returned is put back in the answer variable. So at the end of this, `answer` should contain the value 12.

Having the same variable on both the left and right sides of the `=` sign is actually pretty common and perfectly acceptable. The way to think about it is that on the right side of the `=` we are using the current value of the variable. Then, we put into the variable a new value which is whatever value the expression on the right returns.

There's actually a more compact way to write the same code. Look at this:

```
answer = triple(square(2))
print(answer)
```

This is an example of nesting: we have nested the call to `square()` inside the call to `triple()`. It might be easier to think about if we put in some extra spaces:

```
answer = triple( square( 2 ) )
```

Note: I'm just writing it this way here to make it easier to explain; you shouldn't write it with these extra spaces in your code. Even though it would work, it would be considered poor coding style.

Let's start with the innermost thing, the lone `2` in the center. We're using `2` as the argument (value for the parameter) to `square()`. Then `square()` will return a value and we're using that as the argument to `triple()`.

Remember in the last section where I said that you can imagine the call to the function is replaced by whatever value the function returns?  Let's do that here:

```
answer = triple( square( 2 ) )
```

is equivalent to

```
answer = triple( 4 )
```

is equivalent to

```
answer = 12
```

Whenever you see a nested expression like this, just start from the innermost thing and start applying functions until you get to the outermost thing. This may actually look familiar! In the guessing game we wrote in Lesson 1, we had code that asked for input and converted the input to an integer. It looked like this: `int(input("Enter your guess: "))`. That's actually an example of nested function calls: we are calling the function `input()`, passing it a string prompt, and then passing what it returns to the function `int()` which returns the result converted to an integer.

Each pair of parentheses encloses one level of nesting. Notice at the end, we have two close parentheses (`))`) right after one another. For every open parenthesis, we must have a corresponding close parenthesis and since we have two open parentheses earlier, we must have two close parentheses.

Why are the the two close parentheses right next to each other? Remember that in a function call, the parentheses after a function name wrap the list of the function's arguments. The first open parenthesis after `triple` begins its argument list. Its only argument is the call to `square()` and after that call (which ends with the close parenthesis after `square()`'s argument, `2`'), we must add the close parenthesis for `triple()`'s argument list. It just so happens that this comes right after the close parenthesis for the `square()` argument list.


## Exercises

1. Given the definitions of our `square()` and `triple()` functions above, what would these function calls return?

```
triple(triple(square(2)))
square(square(square(triple(2)))
```

If you're not sure, try working it out by starting from the innermost thing, applying each function going outwards.

2. Can you write a function that returns 1 if the parameter you give it is less than 16 or 0 otherwise?
































