"""
Psuedocode
-----------
1. Create variable to store number of trys.
2. Create list with random words, by importing list file.
3. Choose a random word from list, assign to variable.
4. Loop using trys > 0.
    - Input from user, guessing, check if letter or word.
    - If Letter, check if in random word.
    - If word, check against random word.
    - If correct, show each instance of the letter within the random word.
    - If incorrect, deduct a point from guesses.
    - Once guesses reaches 0, game over.
5. If guesses = 0, game over.
6. If guess = random word, win!
7. Would you like to play again?
8. Try to refactor into functions.
"""

import random
import GuessFunctions

wordlist = GuessFunctions.load_words()
trys = 7
play = True
losses = 0
wins = 0

while play == True:
    rando = random.choice(wordlist)
    used = wordlist.pop(wordlist.index(rando))
    guesses = []
    print('Welcome to the Guessing Game!\n')
    print(f'Current Score: {wins}W / {losses}L')
    while trys > 0:
        
        current = ''
        for letter in rando:
            if letter in guesses:
                current += letter
            else:
                current += "_"
        
        if current == rando:
            print(f'You guessed it! The word was: {rando}!')
            wins += 1
            break

        print (current + '\n')
        temp = input(f'Enter a letter or try to guess the word, {trys} guesses remain!').lower()

        if len(temp) == 1 and temp not in guesses:
            guesses += temp

        if len(temp) > 1:
            if temp == rando:
                print(f'You guessed it! The word was: {rando}!')
                wins += 1
                break
            else:
                trys -=1
                print(f'Incorrect, the word is not {temp}')
        else:
            if temp not in rando:
                trys -= 1
                print(f"There are no {temp}'s")
        
        if trys == 0:
            print('----------- GAME OVER -----------')
            print(f'The word was: {rando}')
            losses += 1
    
    temp = input('Would you like to play again? (yes/no)')
    if temp.lower() == 'yes':
        trys = 7
    else:
        print(f'FINAL SCORE: {wins}W / {losses}L')
        print("Thank you for playing, goodbye!")
        play = False

