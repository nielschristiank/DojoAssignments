
''' print all odd numbers 1 - 1000 '''
for num in range(0,1001):
    if (num%2) != 0:
        print num;

''' print all multiples of 5 from 5 - 1,000,000 '''
for num in range(5,1000001):
    if (num%5) == 0:
        print num;

''' print sum of all values of list '''
a = [1,2,5,10,255,3];
b = 0;
for num in a:
    b += num;
print b;

''' print average of all values of list '''
a = [1,2,5,10,255,3];
b = 0;
for num in a:
    b += num;
b /= len(a);
print b;
