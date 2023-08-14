class user:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(f"User name is {self.name} and age is {self.age}.")


Fahim = user("Md. Fahim Bhuiyan", 22)
Fahim.printInfo()