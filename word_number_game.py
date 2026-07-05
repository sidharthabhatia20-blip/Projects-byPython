a = input("Set a word/number: ")
b = 0
c = 5
while (True):
    print(f"You have {c} chances to enter word correctly")
    b += 1
    print("This is your",b, "attempt")
    d = input("Enter your guess: ")
    if (a.lower() == d.lower()):
        print("You won the game")
        break
    elif c == 1:
        print("You lost! correct word/number was",a)
        break

    c -= 1
