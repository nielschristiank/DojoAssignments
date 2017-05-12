''' FOO BAR '''

def fooBar(num1, num2):
    for i in range(num1, num2+1):
        j = 2;
        while j!=i:
            if i%j==0:
                print "Bar"
            j += 1;
        else:
            print "FooBar"

fooBar(100, 200)
