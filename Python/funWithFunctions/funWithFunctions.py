''''FUN W/ FUNCTIONS '''

'''print if number are odd or even'''
def oddEven(num1, num2):
    for i in range(num1, num2):
        if i%2 != 0:
            print "Number is ", i, ". This is an odd number."
        else: #if i%2 == 0:
            print "Number is ", i, ". This is an even number."

# oddEven(1,2001);

'''iterate list and multiply by a value'''
def multiply(li, num):
    for i in range(0,len(li)):
        li[i] *= num
    return li

y = multiply([2,4,6,8,10], 5)
print y

# '''hacker challenge'''
# def layeredMults(multLi):
#     newLi = []
#     for i in multLi:
#         tempLi = []
#         for j in range(i):
#             tempLi.append(1)
#         newLi.append(tempLi)
#     return newLi

'''hacker challenge'''
def layeredMults(multLi):
    newLi = []
    for i in range(len(multLi)):
        newLi.append([1] * multLi[i])
    return newLi

x = layeredMults(multiply([2,4,5], 3))
print x;
