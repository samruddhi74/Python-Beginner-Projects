import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))

print(f"\n You have 7 chances to get the correct number between {low} and {high}..Let's Start!")

num = random.randint(low, high)
chances = 7
ok = 1

while(chances):
    chances = chances-1
    guess = int(input("Enter your guess: "))

    if(guess == num) :
        print(f"Correct! The number is {num}. You guessed it in {7-chances} attempts.")
        ok = 0
        break
    elif(guess < num):
        print("Too low! Try a higher number")
    else:
        print("Too high! Try a lower number")

if(ok) :
    print(f"The correct number was {num}. Better luck next time!")
