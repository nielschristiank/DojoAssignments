''' TYPE LIST '''

''' test list'''
test = ["hello", 2, 4,"world"];
test2 = ["hello", "world", "yeah"];
test3 = [1,2,3,4,5];
test4 = [0,0,0,'hello'];
test5 = ['','','',4,5];

'''function to test type in list'''
def typeList(li):
    string1 = "";
    string2 = "";
    sm = 0;

    for val in li:
        if isinstance(val, int):
            sm += val;
        if isinstance(val, str):
            string2 += val;
            string2 += " ";

    if all(isinstance(val, int) for val in li):
        string1 = "integer";
        print "The array you entered is of " + string1 + " type";
        print "Sum: ", sm;
    elif all(isinstance(val, str) for val in li):
        string1 = "string";
        print "The array you entered is of " + string1 + " type";
        print "String: " + string2;
    else:
        string1 = "mixed";
        print "The array you entered is of " + string1 + " type";
        print "String: " + string2;
        print "Sum: ", sm;

    # print "The array you entered is of " + string1 + " type";
    # if string2 != "":
    #     print "String: " + string2;
    # if sm:
    #     print "Sum: ", sm;

''' call function to test list'''
typeList(test2);
