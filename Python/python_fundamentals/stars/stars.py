'''STARS!!!!!'''

myLi = [4,6,1,3,5,7,25]
myLi2 = [2,3,54,6,7,8,79,9]

myLi3 = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]

def draw_stars(li):
    for i in li:
        print "*"*i

#draw_stars(myLi)

def draw_stars2(li):
    for i in range(0, len(li)):
        if isinstance(li[i], int):
            print "*"*li[i]
        elif isinstance(li[i], str):
            print li[i][0] * len(li[i])

#draw_stars2(myLi3)

def draw_stars3(li):
    for i in li:
        if isinstance(i, int):
            print "*" * i
        elif isinstance(i, str):
            print i[0].lower() * len(i)

draw_stars3(myLi3)
