#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Hangman Problem
import random
from collections import Counter
 
codeWords = '''cricket badminton volleyball fencing baseball 
football basketball icehockey chess carrom tennis
hockey swimming soccer boxing cycling squash'''
 
codeWords = codeWords.split(' ')
# randomly select a secret word from our "codeWords" LIST.
word = random.choice(codeWords)        
 
if __name__ == '__main__':
    print('Guess the word! HINT: The word is a name of a SPORT!!!')
     
    for i in word:
         # For printing the empty spaces between the letters of the word
        print('_', end = ' ')       
    print()
 
    playing = True
     # list for storing the letters guessed by the player
    letterGuessed = ''               
    chances = len(word) + 3
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed
            print()
            chances -= 1
 
            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('You can enter only a letter!')
                continue
 
            # Validation of the guesses
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess)>1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
 
 
            # If letter is guessed correctly
            if guess in word:
                k = word.count(guess) #variable 'k' stores the number of times the guessed letter occurs in the word
                for _ in range(k):   
                    letterGuessed += guess # The guessed letter is added as many times as it occurs
 
            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end = ' ')
                    correct += 1
                # If user has guessed all the letters correctly
                elif (Counter(letterGuessed) == Counter(word)): # Once the correct word is guessed fully,
                                                                # the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break # To break out from the for loop
                    break # To break out from the while loop
                else:
                    print('_', end = ' ')
 
             
 
        # If user has exhausted all of his chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))
 
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

