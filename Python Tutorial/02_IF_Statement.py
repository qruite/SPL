import random

number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

print(number1, number2)

if (number1 < number2) & (number1 < 50):
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")

elif (number1 < 30) | (number2 < 30):
    print("Eine der beiden ist kleiner als 30")

elif (number1 < 50) & (number2 != 50):
    print("Erste Zahl klein, zweite kein 50iger")
