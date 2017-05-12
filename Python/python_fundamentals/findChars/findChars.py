'''test lists'''

list_test = ['hello','world','my','name','is','Anna'];
char_test = 'o';

# def findChars(li, char):
#     newList = [];
#     for i in range(0,len(li)):
#         for j in li[i]:
#             if char == j:
#                 newList.append(li[i]);
#     print newList;

def findChars(li, char):
    newList = [];
    for i in li:
        for j in i:
            if char == j:
                newList.append(i);
    print newList;

findChars(list_test, char_test);
