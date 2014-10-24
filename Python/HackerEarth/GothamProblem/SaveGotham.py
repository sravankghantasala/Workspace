'''Read Problem.md for the problem.

Created on 24 Oct 2014

@author: sraone
'''

def add_life(hostages, dosage):
    '''Adds life to the given range of hostages with the given aspirin dosage.
    
    Accepts the range of hostages who needs to be given aspirin and the dosage of aspirin needs to be given
    Max limit for adding aspirin is 100, if the life is added beyond 100, it will be always made to 100.
    '''
    global life
    for hostage in hostages:
        life[hostage] += dosage
        if life[hostage] > 100: life[hostage] = 100

def CommandMeGordan():
    '''Gordon commands this guy here.
    '''
    global no_of_hostages,life
#     Iterate until Gordon stops
    while(True):
#         Iterate until Gordon gives you correct command
        while(True):
            try:
#                 Trying because Gordon some times can be nasty and gives you wrong command
                action = int(input('What do you want me to do Gordon? [1/2] ... '))
#                 There are only two commands for you
                if action in [1,2]: break
            except: pass
            print('What the hell is that.. I aint signed for it!')
            
#       If Gordon commands you to give aspirin dosage
        if action == 1:
#             Iterate until gordon tells you the correct hostages and dosage
            while(True):
                try:
#                 Trying because Gordon some times can be nasty and asks you to give crazy dosage or 
#                 to give aspirin to entire Gotham!
                    args = list(map(int,input('Please tell me the range of hostages and the dosage of asprin Gordon ... (x y aspirin) ... ').split()))
                    if len(args) == 3 and args[2] in range(1,101): 
#                         If only Gordon does everything right
                        hostages = range(args[0],args[1]+1)
                        dosage = args[2]
                        add_life(hostages,dosage) #Add life to the given hostages.
                        break
                    else: raise Exception
                except: 
#                     If Gordon behaves crazy
                    print('Please tell me the hostages range and the aspirin for god\'s sake Gordon ! ... ')
                
#         If Gordon asks you for the life info of the hostages
        if action == 2:
            while(True):
#                 Keep asking Gordon until he asks for the real hostages life information
                try:
#                     Trying because Gordon might want to know the life of his relatives living in Africa!
                    args = list(map(int,input('Please tell me the range of hostages to know the life Gordon (x y) ').split()))
                    hostages = range(args[0],args[1]+1)
                    if set(hostages).issubset(range(1, no_of_hostages + 1)) : 
                        print(sum([life[x] for x in hostages])) #Prints the cumulaives lives of the hostages
                        break
                    else: raise Exception
                except: 
#                     When Gordon asks life of non hostages
                    print('Please tell me the hostages range for gods sake Gordon ! ... ')
        if all (x == 100 for x in life.values()) : 
#             If all the hostages were recovered completely
            print('All the hostages were fully recovered Gordon. ')
            break
        print('Lifes of hostages at current stage : ', life)
        cont = input('Do you still think you can save these hostages Gordon ? [y/n] ... ')
        if not cont == 'y': 
            print('Take it easy Gordon, You did your best, but this time its joker\'s')
            break
    
if __name__ == '__main__':
    global life, no_of_hostages
    no_of_hostages = int(input('How many hostages were held by Joker, Gordon ? ... '))
#     Assuming the life of all hostages to be null
    life = dict(zip(range(1,no_of_hostages+1),[0 for i in range(no_of_hostages)]))
    CommandMeGordan()
    print('Thanks for hiring me to save gotham, Gordon!. Time for me to leave... bye.')