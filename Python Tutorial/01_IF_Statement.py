import random

number = random.randint(0, 100)
print(number)

if number <= 20:
    print("Mini")

elif (number > 20) & (number <= 50):
    print("Medium")

elif number > 50:
    print("Large")