import random 
from collections import Counter 

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon kiwi'''

someWords = someWords.split(' ')

word = random.choice(someWords)

if __name__ == '__main__':
    print("Guess the word! Hint: It is a fruit")
    for i in word:
        print('_', end=' ')
    print()
    chances = len(word) + 2
    letterguessed = ''
    flag =0
    try:
        while chances>0 and flag == 0:
            print()
            chances -=1
            try: 
                guess = str(input("Enter a letter to guess: "))
            except:
                print("Enter only a letter!")
                continue

            if not guess.isalpha():
                print("Enter only a letter!")
                continue
            elif len(guess) > 1:
                print("Enter a single letter")
                continue
            elif guess in letterguessed:
                print("You have already guessed this letter")
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterguessed += guess
            
            for char in word:
                if char in letterguessed and (Counter(letterguessed) != Counter(word)):
                    print(char, end=' ')
                elif Counter(letterguessed) == Counter(word):
                    print("You have guessed the word correctly! It is: ", word)
                    flag =1
                    break
                    break
                else :
                    print('_',end=' ')
            if chances == 0 and (Counter(letterguessed) != Counter(word)):
                print("\n Sorry! you lost")
                print("The letter was: ", word)
    except KeyboardInterrupt:
        print()
        print("Bye! Try Again")
        exit()


