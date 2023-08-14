def normal(a, b):
    total = a + b
    return total


result = normal(2, 5)
print(result)


sum1 = normal(4, 10)
print(sum1)


def greeting(name):
    if name == "Alice":
        return "Hello, Alice!"
    elif name == "Bob":
        return "Hi, Bob!"
    else:
        return "Hello, guest!"


print(greeting("Alice"))  # Output: "Hello, Alice!"
print(greeting("Bob"))    # Output: "Hi, Bob!"
print(greeting("Eve"))    # Output: "Hello, guest!"
