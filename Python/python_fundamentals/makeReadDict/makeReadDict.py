'''MAKING AND READINF DICTS'''


myDict = {"name": "Some Dude", "age": 27, "country of birth": "Moon", "favorite language": "Moonspeak"}

def makeReadDict(someDict):
    for key, val in someDict.items():
        print "My",key,"is",val

makeReadDict(myDict)
