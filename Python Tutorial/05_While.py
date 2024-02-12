import random

sum = 0

while True:
    number = random.randint(10, 30)
    print(number)
    if (number == 15) | (number == 25):
        break

    sum += number
    
print("sum = ", sum)