# import random
# number = random.randint(1,100)
number = 15
noOfGuess = 1
maxGuess = 5
while noOfGuess<=maxGuess:
    guess_number = int(input("Guess a Number: "))
    if guess_number<number:
        print("Your guess is low")
    elif guess_number>number:
        print("Your guess is high")
    else:
        print("You Won in !",noOfGuess,"guess")
        break
    print(maxGuess-noOfGuess,"no. of guess left")
    noOfGuess += 1

if noOfGuess>maxGuess:
    print("Game Over!")