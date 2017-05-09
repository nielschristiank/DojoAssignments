#
# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]
#
list_one = [[1,1],[2,2],[3,3]];
list_two = [[1,1],[2,2],[3,3]];
#
# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
#
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
#
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']


def compareLists(list1, list2):

    if list1 == list2:
        print "They are the same!";
    else:
        print "They are different!";

compareLists(list_one, list_two);

# def compareLists(list1, list2):
#     str1 = ""
#     str2 = "";
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 continue;
#             else:
#                 break;
