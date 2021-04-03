# Lesson 01

In Lesson 1, we covered some basics:
* Introduced the Mu editor and the Python Language
* Looked at some examples of games made with PyGame Zero in Mu
* Printed "Hello, world"
* Input
* Variables
* Conditionals (if-statements)
* Made a simple number guessing game
* The `while` loop

Some notes on each of these areas follow.

# Game Examples

All the examples of finished games we looked at can be found at https://github.com/lordmauve/pgzero/tree/1.2release/examples. We looked at FlappyBird, Pong, and Tetra Puzzle.

# Printing

Our very first coding exercise was to print "Hello, world". This is the traditional first step in learning any new programming language. The code we wrote to print this was:

```
print("Hello, world")
```

`print` is a Python function that outputs whatever you give it to the screen. Here we gave it the string "Hello, world" (in computer science, a sequence of characters is called a "string").

We enclosed the words `Hello, world` in quotation marks. This groups those characters together to form a string and tells the Python interpreter not to try to interpret those characters as a Python keyword, a variable name, etc.

We could change the string `Hello, world` to anything else and it would not matter to the python interpreter as long as the string was in quotes.

# Input

Next, we learned about getting input from the user of our program. We typed:

```
input("What is your name?")
```

`input` is another Python function. It takes a string to use as a prompt, prints this string, and then waits for the user to type something as input. When the user presses enter, the program ends.

This was not very exciting because we can't do anything with what the user entered! But we'll fix that in the next section.

Before that it's worth noting two things:

First, when the program ran, and we typed our input, it looked something like this:

```
What is your name?Sam
```

This looks a little awkward because there is no space between the question mark and the text we entered ("Sam"). This is because the string we passed to the `input` function didn't have a space at the end. The computer is doing exactly what we told it to do! This is an important thing to remember and a source of frustration in programming: the computer does exactly what we tell it to do, not what we want it to do. To make it leave a space after the question mark, we changed the code to:

```
input("What is your name? ")
```

The second thing to note is that the prompt we give to `input` is just another string. It's a sequence of characters in quotes and we could change it to anything else, and the Python interpreter wouldn't care.

# Variables
In order to do something with what the user entered when we prompted them for their name, we need to store that somewhere. In programming, we store things in **variables**.

Think of a variable like a container. You can put things in it and you take it what's in it out.

Variables have names. When you use a variable's name in your code, you are telling the Python interpreter to do something with your variable (either put something in it or get the thing that's in it).

Let's store the answer to the "What is your name?" question in a variable:
```
name = input("What is your name?")
```

This tells the Python interpreter to:
* Create a variable called `name`.
* Put into `name` the value that the `input` function returns (this will be the text the user typed in).

Now, we can print a greeting to this specific name as follows:

```
print("Hello " + name)
```

When you run the program now, it should prompt for your name and then print "Hello ", followed by your name. In the print statement above, when we referenced the variable `name` it tells the Python interpreter to grab whatever is currently stored in the variable `name` and replace `name` in that statement with that value.

For example, if the variable `name` stored the string, "Sam", Python would treat the above statement as if you had said:

```
print("Hello " + "Sam")
```

(Notice that space at the end of the string "Hello ": without it, the program will print something like `HelloSam`.)

Generally every programming language will have some rules about what a variable name can be. We don't need to go into all these rules now as long as you remember that your variable should NOT:
* Have the same name as a Python keyword or function name (like "print")
* Start with anything besides a letter
* Have spaces in it

# Conditionals
Let's add some code to ask the user their age and store what they type into a variable called `age`:

```
age = input("What is your age? ")
```

Now, let's say we want our program to make a choice: to do one thing in some situations and another thing in others. As an example, the cousins once wanted to keep the adults out of their play area. They made a sign that said "No one over age 16 allowed".

Let's implement that sign in code. What we want to express in Python is this:
* If their age is less than 16, print a message saying you're allowed in.
* Otherwise, print a message saying you're not allowed in.

The way we express things like this in Python is with an **if-statement**. The if-statement that implements the logic described above looks like this:

```
if int(age) < 16:
    print("You are allowed in")
else:
    print("You are NOT allowed in")

```

Ignore the `int()` around the variable `age` for just a second. I'll explain it shortly.

What the first line says is "if the value stored in the variable `age` is less than 16". We then want to tell the Python interpreter what to do in that case.

Notice that the `if` line ends in a colon (`:`) and that the line after it is indented by 4 spaces. This has special meaning in Python. The colon means that what follows is one or more statements that all "belong" together with the line above it. Here, the line `    print("You are allowed in")` belongs with the line `if int(age) < 16:`. Python will only run the line `    print("You are allowed in")` if the value in the `age` variable is less than 16.

Now let's look at the `else` part of the statement. Remember, what we are trying to express is to print one message if the age is less than 16, *otherwise* print a different message. In Python, `else` means "otherwise".

Notice again that the `else:` line ends in a colon and that the line following it is indented 4 spaces. This has the same meaning. The colon indicates that the line following belongs with the `else:` line. Python only runs that line if the age *isn't* less than 16.

Now back to that weird `int(age)` thing. Why is that there? Notice that our program is treating the value in the variable `age` as a number by comparing it to 16. It only makes sense to compare one number to another. What would it mean to compare the string "banana" to 16?\*. But, when we asked the user to enter their age, they could well have entered "banana".

I told you before to remember that the computer always does exactly what you tell it to do, not what you want it to do. You should also remember that the users of your program do whatever they want to do, not what you intended them to do. So when you asked their age, expecting them to enter a number, they could well have entered something that isn't a number.

\*Note, in some programming languages, expressions like "banana" < 16 actually do have a specific meaning, but you don't need to worry about that right now.

Let's say we had written our if-statement without the `int()` thing. It would have looked like this:

```
if age < 16:
    print("You are allowed in")
else:
    print("You are NOT NOT NOT NOT allowed in")
```

If you try to run this, you'll get an error. Something like:

```
Traceback (most recent call last):
  File "/Users/spather/mu_code/lesson1.py", line 7, in <module>
    if age < 16:
TypeError: '<' not supported between instances of 'str' and 'int'
```

Because the Python interpreter knows it won't be able to do a sensible thing if the value in the variable `age` is "banana" and you ask it to compare that to 16, it will give you an error.

Seeing errors like this can be scary and frustrating when you're new to programming. Try not to be scared of them. These messages are the Python interpreter trying to help you by pointing out something that could go wrong.

Here, the last line of the error message `TypeError: '<' not supported between instances of 'str' and 'int'` contains the key. In English, it's saying that it can't do less-than (`<`) between something that is a string (`str`) and an integer (`int`). (If you don't know the term `integer` it just means a whole number like 5 or 17 or 127323, but not a fractional number like 1.2332.).

By wrapping `age` in a call to the function `int()` we are telling Python to turn the string value of the variable `age` into an integer. Even if the user typed a number like 10, technically the value in the variable `age` would be the string "10", which the computer stores differently than the integer 10. Calling the `int()` function turns the string "10" into the integer 10.

Note: when I mentioned the function `int()` I have an open and close parenthesis after the name. This is a writing convention that conveys that something is a function, as opposed to a variable or something else. I didn't use this convention when I referred to the `print()` function has just `print` before but I'll refer to all functions this way going forward.

What if the user had typed "banana" instead of a number like "10"? Well, then Python would give you a different error:

```
Traceback (most recent call last):
  File "/Users/spather/mu_code/lesson1.py", line 7, in <module>
    if int(age) < 16:
ValueError: invalid literal for int() with base 10: 'banana'
```

Again, the scary looking error is actually trying to help by telling us something important. Look at the last line: It's telling us that 'banana' is an invalid literal for `int()` to convert as a base 10 number. If you're wondering what a "literal" is, it's a programming language word that basically means a value, like "banana".

Now, you might be wondering, why did we go to all this trouble if we could get an error either with or without the call to int(). The answer is that, without the `int()` we got an error no matter what the user entered for their age. Because Python can't know in advance what they'll enter, and knowing that it might be something it can't compare to 16, it just raises an error, every time. But with the `int()` we only get the error if the value the user enters is something that's not a number. This is kind of what we want to happen. Later, we'll learn about how to give the user nicer error messages but for now, it's a good thing if our program fails when the user enters something we can't process.

# Making a Simple Guessing Game

With what we know so far, we can make a simple text-based game that works like this:
* We decide on a "secret number" in advance
* We ask the user to guess our secret number
* If the number they guess is too low, we'll print a message telling them that.
* If the number they guess is too high, we'll print a message telling them that.
* If the number they guess is our secret number, we'll print a message telling them they guessed correctly.

The basic logic of this puts together everything we've learned so far: printing, getting input, using variables, and an if-statement.

Let's turn our description of the game into Python code:

```
secret_number = 57
guess = int(input("Enter your guess: "))
if guess < secret_number:
    print("Too low")
elif guess > secret_number:
    print("Too high")
else:
    print("Congrats, you got it!")
```

The first line just creates a variable called `secret_number` and puts the value 57 into it. Remember earlier when I said that variables can't have spaces in them? A common way programmers get around that is to put underscores (\_) where the spaces would go.

Next, we use the `input()` function to ask the user to enter a number. Like before, we want this input to be a number (an integer more specifically), so we wrap the call to `input()` with a call to `int()`. What this is doing is taking the result from the call to `input()` (the value the user entered) and passing it to `int()` before storing it in the variable `guess`. Don't worry too much if this is confusing; this is an example of something called nested function calls, which we'll learn about next week. Just know that at the end of this, the variable `guess` contains the value that the user entered, stored as an integer. If the user entered something that isn't a number, the program will give an error, just like before.

After getting the user's guess into the variable `guess` we have an if-statement. This one works just like the last one. The `if` line ends in a colon, indicating the next indented line goes with it. If the guess is less than the secret number, we print the message "Too low".

The next line introduces a new keyword, `elif`. Remember the if statement we saw earlier which had an `else` clause in it which meant "otherwise"? `elif` is short for "else if". It's a little more specific than "else" or "otherwise" which basically mean "in all other cases". `elif` is a way to express another "if" that is evaluated if the first one isn't satisfied.

The line `elif guess > secret_number:` is saying: assuming the condition in the if-statement (`guess < secret_numer`) isn't true, then check another condition: `guess > secret_number`. If that is true, then do the following, indented line: `print("Too high")`.

Lastly, we have a final `else` clause. The indented statement after it runs if the conditions in the `if` and the `elif` weren't true. In this example, if guess wasn't less than the secret number and it wasn't greater than the secret number then it must be equal to the secret number and we print a congratulations message.

Note that an if-statement must always have the `if` line, may have zero, one, or many `elif` clauses, and zero or one `else` clause.

If we run the program now, it should ask for a guess and print the appropriate message based on whether the guess was too low, too high, or just right. But that isn't really a guessing game. It just gives the user one shot at making the right guess. What we want to do is to let the user keep guessing and give them the too high/too low messages for each guess until they get it right. To do this, we need to introduce another concept: a `while` loop.

# While Loops

In programming languages, a *loop* is something that helps you make blocks of code run over and over again. In this section, we're going to learn about one kind of loop: a `while` loop.

A while loop is a little like an if-statement. The while statement contains a condition, just like the if-statement. But where an if-statement only runs the block of code following it if the condition is true, the while loop runs the block of code following it, over and over, until the condition is true.

This will be easier to understand with an example. Change the code you have for the guessing game to look like this:

```
secret_number = 57
guess = 0
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Congrats, you got it!")

```

(Notice that the code after the `while` line is the same as the code we just entered in the previous section, except that it is intended. If you want to re-use the code you entered, the Mu editor will let you highlight the whole block and press TAB once to indent it all.)

As before, we assign a number to a `secret_number` variable. The next line assigns the value 0 to the `guess` variable. Ignore this for the moment: I'll explain why we need this shortly.

Then we have the while loop. It consists of the word `while` followed by a condition. Here the condition is `guess != secret_number`. This means: the value in the variable `guess` is not equal to the value in the variable `secret_number`. In Python, `!=` means "not equal to". It kind of looks like the ≠ symbol you may know from math classes.

Notice that the `while` line ends with a colon, and that the lines following it are indented. As with if-statements, the colon indicates that the following indented lines belong with the `while` line. The `while` loop will run the indented block of code following it as long as the condition specified in the while statement (`guess != secret_number` in our case) is true. Breaking this down:

1. The while loop evaluates its condition.
2. If the condition is true, then it executes the block of indented lines below it. If the condition is false, then the loop is finished: the program will then run the next line of code that is at the same level of indentation as the `while` statement itself, if there is one.
3. After all of the lines in the indented block below the `while` have run, the process returns to step 1.

In our while loop, the indented block of lines, which ask the user for a guess and then tell the them if their guess is too high, too low, or right, executes over and over until the guess is equal to the secret number. This is what we want: the user should be asked to guess, and told how their guess fares, until they get the right answer.

Notice that within the block of code that is intended after the `while`, there are some lines, specifically those beneath the `if`, `elif`, and `else` lines, which are indented a level further. This is because the if-statement itself is part of the block of code associated with the `while` loop, but within the if statement, there are parts associated with the `if`, `elif`, and `else` parts specifically. They are nested further to indicate this relationship.

Remember the line near the top that reads `guess = 0` which I said we'd come back to? Why do you think we need this? Try removing that line and see what error you get. Can you make sense of this error?

The error message should look like this:

```
Traceback (most recent call last):
  File "/Users/spather/mu_code/lesson1.py", line 13, in <module>
    while guess != secret_number:
NameError: name 'guess' is not defined
```
Again, this is the Python interpreter trying to help is. Look at the last line: it tells us that the name `guess` is not defined. This means that Python has encountered our use of the word `guess` in the while-loop statement but since we have not yet created a variable called `guess` Python doesn't know what this is. Python (and other programming languages) will never try to guess (pardon the pun) what you mean by a word it doesn't recognize. Here we have to tell it that guess is a variable and we do that by simply assigning it a value of 0 (`guess = 0`). We could really have used any number that isn't the value we assigned to `secret number`.

This practice, of giving a variable some value to start with, is called **initialization**. What do you think would have happened had we initialized `guess` with the same value as our secret number?












































