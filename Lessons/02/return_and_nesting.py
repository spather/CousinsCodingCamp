# Functions can return values.
def square(num):
    return num * num

def triple(num):
    return num * 3

# Function calls can be nested.
answer = triple(square(2))
print(answer)
