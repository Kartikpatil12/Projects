import random

def play():
    while True:
        x = input("Enter you choice: ").lower()
        l = ["rock","paper","scissor"]
        choice = random.choice(l)
        print("Computer signed ",choice)
        if x == "end":
            break
        if choice == "rock" :
            if x == "paper":
                print("Paper cover rock, You win!")
            elif  x == "scissor":
                print("Rock crushed scissor , You loose!")
            else:
                print("match tied , Try again")
                play()

        if choice == "paper" :
            if x == "rock":
                print("Paper cover rock, You loose!")
            elif  x == "scissor":
                print("Scissor cut paper, You win!")
            else:
                print("match tied , Try again")
                play()


        if choice == "scissor" :
            if x == "paper":
                print("Scissor cut paper, You loose !")
            elif  x == "rock":
                print("Rock crushed scissor , You win!")
            else:
                print("match tied , Try again")
                play()
        print("\r")


if __name__ == '__main__':
    print("let's play")
    play()
