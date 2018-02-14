#inserting the random function
import random

#assuming ctr as 0
ctr=0
print('welcome lets begain the game of s&l ')
print('your current position is',ctr)
while(ctr<100):
    r=random.randint(1,6)
    j=input('press enter to roll the dice')
    ctr=ctr+r
    print('your current position is',ctr)
    #if condition ctr moves from 8 to 37
    if ctr==8:
        ctr=37
        print('you climbed the ladder from 8 to 37')
    #elif condition ctr moves from 13 to 34
    elif ctr==13:
        ctr=34
        print('you climbed the ladder from 13 to 34')
     #elif condition ctr moves from 40 to 68
    elif ctr==40:
        ctr=68
        print('you climbed the ladder from 40 to 68')
     #elif condition ctr moves from 52 to 81        
    elif ctr==52:
        ctr=81
        print('you climbed the ladder from 52 to 81')
    #elif condition ctr moves from 76 to 97       
    elif ctr==76:
        ctr=97
        print('you climbed the ladder from 76 to 97')
    #elif condition ctr moves from 11 to 2
    elif ctr==11:
        ctr=2
        print('snake bites you move from 11 to 2') 
     #elif condition ctr moves from 25 to 4
    elif ctr==25:
        ctr=4
        print('snake bites you move from 25 to 4')
      #elif condition ctr moves from 38 to 9
    elif ctr==38:
        ctr=9
        print('snake bites you move from 38 to 9')
      #elif condition ctr moves from 65 to 46
    elif ctr==65:
        ctr=46
        print('snake bites you move from 65 to 46')
       #elif condition ctr moves from 89 to 70
    elif ctr==89:
        ctr=70
        print('snake bites you move from 89 to 70')
        #elif condition ctr moves from 93 to 64
    elif ctr==93:
        ctr=64        
        print('snake bites you move from 93 to 64')
print("YOU WON")
    
