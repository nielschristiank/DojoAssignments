''' CARS '''

class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    def display_all(self):
        print "Price:",self.price
        print "Speed:",self.speed
        print "Fuel:",self.fuel
        print "Mileage:",self.mileage
        print "Tax:",self.tax
        print "\n"
        return self

car1 = car(2000, "35mph", "Full", "15mpg")
car2 = car(2000, "5mph", "Not Full", "5mpg")
car3 = car(2000, "35mph", "Full", "65mpg")
car4 = car(11000, "45mph", "Empty", "55mpg")
car5 = car(2000, "35mph", "Full", "10mpg")
car6 = car(20000, "35mph", "Full", "1mpg")
