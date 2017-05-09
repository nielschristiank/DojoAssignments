
# Find and Replace
str = "It's thanksgiving day. It's my birthday,too!";
print str.find("d");
print str.replace("day", "month");

# Min and Max
x = [2,52,-2,7,12,98];
print min(x), max(x);

# First and Last
y = ["hello", 2,54,-2,12,98,"world"];
print y[0], y[len(y)-1];

# New List
z = [19,2,54,-2,7,12,98,32,10,-3,6,94,59,59,699,6,5,"hello"];
z.sort();
z_1 = [];
for num in z[0:(len(z)/2)]:
    z_1.append(num);
    z.remove(num);
z.insert(0, z_1);
print z;
