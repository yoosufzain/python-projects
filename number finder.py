import random 

def game():
    level = input("Enter level Medium(m),Hard(h)")
    if level == "m":
        Number = random.randint(1,50)
    else:
        Number = random.randint(1,100)
    Attempt = 10
    print(f"Attempts:{Attempt}")
    while True:

        try :
            guessed_number = int(input("What is your guess number?"))
        except ValueError:
            print("EnterEnter a valid number!")
            Attempt -=1
            print(Attempt)
        
        else:
            if guessed_number > Number:
                print("High")
            elif guessed_number< Number :
                print("Low")
        
            else :
                print("Yeah great it is correct answer")
                return
            Attempt -=1
            print(Attempt)    
            if Attempt == 0:
                print("Game over!")
                return
game()
while True:
    restart = input("Do you want to start again [y/n].")
    if restart in "Yy":
        game()
    else :
        exit()
