# Write your code here :-)
print("Hello, world")
name = input("What is your name? ")
print("Hello " + name)

age = input("What is your age? ")
if int(age) < 16:
    print("You are allowed in")
else:
    print("You are NOT NOT NOT NOT allowed in")

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


