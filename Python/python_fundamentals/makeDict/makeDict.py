
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(li1, li2):
    newDict = dict(zip(li1, li2))
    print newDict

make_dict(name, favorite_animal)
