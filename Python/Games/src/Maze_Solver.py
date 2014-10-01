'''
Created on 29 Sep 2014

@author: sraone
'''
from random import shuffle
import os

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
        move=int(input('Please enter your move ... '))
        if move in range(1,size*size): break
    return move


def move_me(move,data,size):
    zero_index=data.index('_')
    num_index=data.index(move)
    delta=abs(num_index - zero_index)
    if (delta in [1,size]):
        data[zero_index] = move
        data[num_index] = '_'
        


def maze_looper(size,orig):
    data=orig
    moves=0
    while (game_over(data,size)):
        maze_printer(size, data, moves)
        move_me(get_move(size),data,size)
        moves+=1
        
        
def print_banner(moves):
    print('*'*80)
    print('*','Simple Maze'.center(76),'*')
    print('*'*80)
    print('\n\n')
    print(('Total Moves : {0}'.format(moves)).center(80))
    print('\n\n')


def maze_printer(size,data,moves):
#     Clearing screen
    os.system('cls')
    os.system('clear')
    print_banner(moves)
    count=0
    for i in data:
        print(str(i).center(8), end='')
        count+=1
        if count==size :
            print()
            count=0
        

if __name__ == '__main__':
    print_banner(0)
    size=get_size()
    orig=[i for i in range(1,size*size)]
    orig.append('_')
    shuffle(orig)
    maze_looper(size,orig)