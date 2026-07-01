print("Program 1")

def greet():
    print("Hello, Preet!")

greet()

print("-----------------")

print("Function with a parameter")

def greet(name):
    print("Hello,", name)

greet("Preet")
greet("Luffy")
greet("Zoro")
greet("Sanji")

print("----------------")

print("Function that returns a value")

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

print("------------------")