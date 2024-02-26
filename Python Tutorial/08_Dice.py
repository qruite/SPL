import random
import sys

remainingAttempts = 6
gameState = True
sumPlayer = 0
sumComputer = 0
state = True


def getResult():
    print("Augensumme Spieler: ", sumPlayer)
    print("Augensumme Computer: ", sumComputer)
    print("--------------------------")
    
    if(sumPlayer > sumComputer):
        print("Spieler hat gewonnen")
    elif(sumPlayer == sumComputer):
        print("Unentschieden")
    else:
        print("computer hat gewonnen")
    
    print("--------------------------")
    print("")


def start():
    global remainingAttempts, sumPlayer, sumComputer, state

    while state:
        print("remaining attempts:", remainingAttempts)
        print("--------------------------")
        print("1. würfeln")
        print("2. beenden")
        print("--------------------------")

        n = int(input())

        if remainingAttempts == 1:
            state = False
            getResult()
        elif n == 1:
            remainingAttempts -= 1
            playerResult = random.randint(1, 6)
            print("spieler: ", playerResult)
            computerResult = random.randint(1, 6)
            print("computer: ", computerResult)
            sumPlayer += playerResult
            sumComputer += computerResult
        elif n == 2:
            state = False

while gameState:
    print("willkomen")
    print("--------------------------")
    print("1. starten")
    print("2. beenden")
    print("--------------------------")

    n = int(input())

    if n == 1:
        start()
    elif n == 2:
        gameState = False
