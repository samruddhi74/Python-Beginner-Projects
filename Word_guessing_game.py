import random

name = input("Hey! what can we call you?")
print("Good luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")

guesses = ''
chances = 12

while(chances):
    failed =0
    for char in word :
        if char in guesses:
            print(char, end = " ")
        else:
            print("_")
            failed += 1
    if(failed == 0):
        print("You win")
        print("The word is: ",word)
    print()
    guess = input("guess a character:")
    guesses += guess

    if(guess not in word):
        chances -= 1
        print("Wrong")
        print("You have" , chances, "more guesses")

        if(chances == 0):
            print("You lose")
            print("The word was ", word)