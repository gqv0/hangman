# cd into Hangman folder and run py
# can enter both full word guesses and letters
# full word guesses don't count in max_wrong

import random
import csv

words = []
guesses = []

wrong = 0
max_wrong = 6

with open("wordbank.csv", "r") as file:
    reader = csv.reader(file, skipinitialspace = True)
    for x in reader:
        words.extend(x)

word = random.choice(words) # sets the secret word for the match

while wrong < max_wrong:

    current_word = "" # sets your guesses and blank letters

    for letter in word:
        if letter in guesses:
            current_word += letter
        else:
            current_word += "_"

    # check if u won using the lack of "_"
    if "_" not in current_word:
            print(f"Correct! The word was: {word}")
            break


    # gui
    print(f"Your word: {current_word}")
    print(f"Guessed Letters: {', '.join(guesses)}\n{wrong} out of {max_wrong} wrong.")

    i = input("Guess: ")
    i = i.lower()

    print(".-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.")

    # checking if guess is valid or contains the full word,,, yes it's ugly
    if i == word:
        print(f"Correct! The word was: {word}")
        break
    elif i in guesses:
        print("Already guessed that!")
    elif len(i) > 1:
        print("Guess is too long!")
    elif not i.isalpha():
        print("Only enter letters!")
    elif i in word:
            print(f"CORRECT! ✔ {i} is in the word.")
            guesses.append(i)
    else:
            print(f"WRONG. {i} is not in the word.")
            guesses.append(i)
            wrong += 1

    
else: # losing condition 
    print(f"You lost. \nThe word was: {word}.")