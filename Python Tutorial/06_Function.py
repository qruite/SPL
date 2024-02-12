import random

words = ["Tastatur", "Handy", "Apfel", "Tisch"]

def add(a, b):
    return a + b

def Random():
    number = random.randint(100, 200)
    return number

def getWordFromArray():
    number = random.randint(0, 3)
    return words[number]


print(add(5, 6))
print(Random())
print(getWordFromArray())