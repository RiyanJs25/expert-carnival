def greet():
    name = input("What's your name? ")
    return f"Hello, {name}! Welcome to debugging mode."

def add_numbers(a, b):
    result = a + b
    return result

print("Program started")
sum_value = add_numbers(5, 7)
print("Sum:", sum_value)

# Breakpoint example
print(greet())

print("Program ended")
