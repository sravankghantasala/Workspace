

    A large network of criminals is working under JOKER to destroy and demolish Gotham city. Captain Gordon is quite tensed about what these criminals can do to Gotham city. Fortunately, Batman comes to his rescue and with the help of the Batman, he was able to rescue N hostages that were trapped by the criminals working under JOKER. He makes them stand in a line and each of the N hostage is given id between 1 to N (inclusive) and no 2 hostages have same id. You are a newly hired programmer who is assigned the task of keeping track of the health status of hostages as Captain Gordon heals them by giving them aspirin each time. Initially,health of each hostage is 0. He then performs following action -

    • Gives Aspirin of value v to hostages having id between x and y (both inclusive) which increaces their present health by v.

    • He asks you to give him the sum of the health of all the hostages having id between x and y (both inclusive) Can you write a program which keeps track of Gordon’s action?

    INPUT 1st Line contains N-no. of hostages 2nd line contains M-no. of actions performed by Captain Gordon. The next M lines contain the actions in the form of either “ 1 x y v “ which denotes Action 1 or “ 2 x y “ which denotes Action 2.

    OUTPUT For each action that Captain Gordon does, if Action 1 is carried out, output nothing but if Action 2 is carried out, the program must output the result that Gordon asks for.

    CONSTRAINTS

    1) N<=10^5

    2) M<=10^5

    3) 1<=x < y<=N

    4) 0<=v<=100

Sample Input
5
6
2 1 5
1 3 4 5
2 2 4
1 1 3 10
1 1 5 5
2 1 5

Sample Output
0
10
65
