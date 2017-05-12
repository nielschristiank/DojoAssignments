''' BIKES '''

class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles > 5:
            self.miles -= 5
        return self

bike1 = bike(200, "25mph")
bike2 = bike(300, "35mph")
bike3 = bike(400, "45mph")

print bike1.displayInfo().ride().ride().ride().reverse().displayInfo()
print bike2.displayInfo().ride().ride().reverse().reverse().displayInfo()
print bike3.displayInfo().reverse().reverse().reverse().displayInfo()



# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = True
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
#     def logout(self):
#         self.logged = False
#         print self.name + " is not logged in"
#         return self
#     def show(self):
#         print "My name is {}. You can email me at {}".format(self.name, self.email)
#         return self
