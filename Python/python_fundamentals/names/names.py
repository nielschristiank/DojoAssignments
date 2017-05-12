'''NAMES'''


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def outputStudents(someDict):
    for i in someDict:
        name = ""
        for val in i:
            name = name + i[val] + " "
        print name

#outputStudents(students)

def outputStudsInts(someDict):
    for key in someDict:
        print key
        count = 1
        for key2 in someDict[key]:
            name = ""
            for val in key2:
                name = name + key2[val] + " "
            print count,"-",name,"-",(len(name)-2)
            count += 1
outputStudsInts(users)
