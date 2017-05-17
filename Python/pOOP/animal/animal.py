class animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Animal:", self.name
        print "Health:", self.health
        print "\n"
        return self

class dog(animal):
    # def __init__(self, pet_name):
    #     self.name = "Dog"
    #     self.pet_name = pet_name
    #     self.health = 150
    def __init__(self, pet_name):
        self.name = "Dog"
        self.pet_name = pet_name
        self.health = 150
    def pet(self):
        self.health += 5
        return self
    def displayHealth(self):
        print "Name:", self.pet_name
        super(dog, self).displayHealth()
        return self

class dragon(animal):
    def __init__(self, dragon_name):
        self.name = "Dragon"
        self.dragon_name = dragon_name
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "I AM DRAGON!"
        print "Name:", self.dragon_name
        super(dragon, self).displayHealth()
        return self

tiger = animal("Tiger")
tiger.displayHealth().walk().walk().walk().run().run().run().displayHealth()

hazel = dog("Hazel")
hazel.displayHealth().walk().walk().run().run().displayHealth()

drogo = dragon("Drogo")
drogo.displayHealth().fly().fly().fly().displayHealth()
