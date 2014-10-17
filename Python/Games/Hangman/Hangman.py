'''
Created on 17-Oct-2014

@author: ghantasa
'''
from random import randint
import time

WORD = ''
GUESSWORD = list()
LIVES = 0

# Get Word
def get_word():
# Select Grade
    while(True):
        grade = input('Please enter the grade that you want to play the game ... (1/2/3) ')
        if int(grade) in range(1,4): break
# Find a word from the selected grade.
    with open("Words/"+grade) as f:
        lines = f.readlines()
        word=lines[randint(0,len(lines))]
        
    return word.strip()

# Get all the occurances of a letter in the word
def get_indices(letter):
    indices = list()
    for i in range(0,len(WORD)):
        if WORD[i] == letter: indices.append(i)
    
    return indices

# Modify Guess Word
def modify_guessWord(letter):
    flag = False
    indices = get_indices(letter)
    for index in indices:
        if not GUESSWORD[index] == letter:
            GUESSWORD[index] = letter
            flag=True
    return flag

# Print structure
def print_structure():
    print(WORD)
    print("Your Guess Word : ",' '.join(GUESSWORD))
    print("No of lives still : ", LIVES)
    
# Check if the game is completed
def incomplete():
    if ( ''.join(GUESSWORD) == WORD): return False
    else: return True
    
def Hangman():
    global WORD, LIVES, GUESSWORD
    WORD = get_word()
    LIVES = len(WORD)
    GUESSWORD = list('_'*LIVES)
    
    while(True):
        if(incomplete()):
            print_structure()
            if not modify_guessWord(input('Please enter your choice letter ... ')) :
                LIVES-=1
                print('Wrong choice...!')
                if LIVES <= 0 :
                    print('You ran out of your lives .. You will be hanged now .. Rest in Peace!')
                    break
                time.sleep(1) 
        else:
            print('Woohoo!, You finished your game ... Congratualtions.')
            break
    
if __name__ == '__main__':
    Hangman()
        
        


    