'''
Created on 29 Sep 2014

@author: sraone
'''
from random import shuffle
import os
import sys
import time

def get_size():
    size=int(input('Enter the size of the maze you want to play ... '))
    while not size in range(3,17):
        print('Sorry I cannot provide this kind of maze for you! ... ')
        size=int(input('Enter the size of the maze you want to play ... ')) 
    return size


def game_over(current,size):
    result=[i for i in range(1,size)]
    result.append('_')
    if current == result: return False
    else: return True


def get_move(size):
    while(True):
        move=int(input('\nPlease enter your move ... '))
        if move in range(1,size*size): break
    return move


def move_me(move,data,size):
    moved = False
    
    zero_index=data.index('_')
    num_index=data.index(move)
    
#     If number is at the left extreme of the row, the last number from the previous row should not be moved.
#     Identify if the index is left extreme.
    if (zero_index % size == 0):
        delta=(num_index - zero_index)
        if (delta in [1,size,-size]):
            data[zero_index] = move
            data[num_index] = '_'
            moved = True
    
#     If number is at the right extreme of the row, the first number from the next row should not be moved.
#     Identify if the index is right extreme. 
    elif (zero_index % size == (size-1)):
        delta=(num_index - zero_index)
        if (delta in [-1,size,-size]):
            data[zero_index] = move
            data[num_index] = '_'
            moved = True

#     If number is not at any extremes.
    else:
        delta=abs(num_index - zero_index)
        if (delta in [1,size]):
            data[zero_index] = move
            data[num_index] = '_'
            moved = True
    
    return moved


def maze_looper(size,orig):
    data=orig
    moves=0
    while (game_over(data,size)):
        maze_printer(size, data, moves)
        if move_me(get_move(size),data,size): moves+=1
        else: print('Invalid move!'); time.sleep(1)
            
def print_banner(moves):
    print('*'*80)
    print('*','Simple Maze'.center(76),'*')
    print('*'*80)
    print('\n\n')
    print(('Total Moves : {0}'.format(moves)).center(80))
    print('\n\n')


def maze_printer(size,data,moves):
#     Clearing screen
    if 'win' in sys.platform : os.system('cls')
    elif 'linux' in sys.platform : os.system('clear')
    print_banner(moves)
    count=0
    for i in data:
        print(str(i).center(8), end='')
        count+=1
        if count==size :
            print()
            count=0

def maze_solver():
    print_banner(0)
    size=get_size()
    orig=[i for i in range(1,size*size)]
    orig.append('_')
    shuffle(orig)
    maze_looper(size,orig)

if __name__ == '__main__':
    maze_solver()