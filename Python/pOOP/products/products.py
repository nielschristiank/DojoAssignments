''' PRODUCTS '''


class product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold"
        return self
    def addTax(self):
        self.price += (self.price * 0.0975)
        return self
    def returnProduct(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "like new":
            self.status = "For Sale"
        elif reason == "opened":
            self.status = "Used"
            self.price = self.price * 0.8
        return self
    def displayInfo(self):
        print "Product:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        print "Cost:", self.cost
        print "\n"
        return self

flatScreenTV = product(1499.95, "1080p HDTV", "20lbs", "SONY", 800)

flatScreenTV.displayInfo().addTax().displayInfo().sell().displayInfo().returnProduct("opened").displayInfo()
flatScreenTV.displayInfo().addTax().displayInfo().sell().displayInfo().returnProduct("like new").displayInfo()
flatScreenTV.displayInfo().addTax().displayInfo().sell().displayInfo().returnProduct("defective").displayInfo()
