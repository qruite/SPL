import sys

balance = 5000

def deposit():
    print("geben Sie Betrag ein, den Sie einzahlen möchten")
    depositAmount = float(input())
    return depositAmount

def withdrawl():
    print("geben Sie Betrag ein, den Sie auszahlen möchten")

    state = True
    while state:
        withdrawlAmount = float(input())

        if (balance - withdrawlAmount) < 0:
            print("!!!!nicht genug Guthaben!!!!")
            print("ihr aktueller Kontostand", balance)
            print("-----------------------------------")
            print("geben Sie neuen Betrag ein, den Sie auszahlen möchten")
        else:
            state = False

    return withdrawlAmount


def Balance(balance):
    print("Kontostand:", balance)
    

def finish():
    print("Aufwiedersehen")
    sys.exit()

while True:
    print("1. Einzahlen")
    print("2. Abheben")
    print("3. Kontostand")
    print("4. Beenden")
    
    n = int(input())

    if n == 1:
        balance += deposit()
    elif n == 2:
        balance -= withdrawl()
    elif n == 3:
        Balance(balance)
    elif n == 4:
        finish()
        

    
    