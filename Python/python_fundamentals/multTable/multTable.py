'''Multiplication Table'''

def multTable(num1, num2):

    for row in range(num1,num2+1):
        if (row < 10):
            print row," ",
        elif(row < 100):
            print row, "",
        else:
            print row,
        for col in range(num1, num2+1):
            if ((row*col) < 10):
                print row*col," ",
            elif((row*col) < 100):
                print row*col,"",
            else:
                print row*col,
            #print row*col,
        print ""
    #print row

multTable(1,12)
