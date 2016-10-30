# Method 1
def factorial(input):
    if input == 0:
        return 1
    else:
        return input * factorial(input-1)

# Method 2
def factorial(input):
    result = 1
    while input >= 1:
        result = result * input
        input = input - 1
    return result

print factorial(5)