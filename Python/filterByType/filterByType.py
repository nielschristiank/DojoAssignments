''' variables to test '''
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

''' function to print statement if number is >, or < 100 '''
def whatAmAndHowBig(val):
    if isinstance(val, int):
        if val >= 100:
            print "Big Number";
        elif val < 100:
            print "Small Number";
    elif isinstance(val, str):
        if len(val) >= 50:
            print "Long Sentence";
        elif len(val) < 100:
            print "Short Sentence";
    elif isinstance(val, list):
        if len(val) >= 10:
            print "Big List";
        elif len(val) < 10:
            print "Short List";

''' call function for all test variables'''
whatAmAndHowBig(sI);
whatAmAndHowBig(mI);
whatAmAndHowBig(bI);
whatAmAndHowBig(eI);
whatAmAndHowBig(spI);
whatAmAndHowBig(sS);
whatAmAndHowBig(mS);
whatAmAndHowBig(bS);
whatAmAndHowBig(eS);
whatAmAndHowBig(aL);
whatAmAndHowBig(mL);
whatAmAndHowBig(lL);
whatAmAndHowBig(eL);
whatAmAndHowBig(spL);
