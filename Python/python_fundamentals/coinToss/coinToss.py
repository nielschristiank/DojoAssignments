
import random

def coinToss(num):
    heads = 0
    tails = 0
    for i in range(num):
        randNum = round(random.random())
        if randNum == 0:
            heads += 1
            #print "Attempt #",i,": Throwing a coin... It's a head! ... Got ",heads," head(s) so far and ",tails," tail(s) so far"
        elif randNum == 1:
            tails += 1
        print "Attempt #",i,": Throwing a coin... It's a head! ... Got ",heads," head(s) so far and ",tails," tail(s) so far"
    print "Ending the program, thank you!"


coinToss(5000)
