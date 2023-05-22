# object oriented programming
# final programming task - creating of such a subject, but also writing to a program, text analysis and so on
# data attributes and procedural attributes

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return "Animal name: "+str(self.name)+", age: "+str(self.age)


# parent class
# animec = Animal(10)
# animec.name = "Animec"
# animec.age = 12
# print(animec)

# anima = Animal(18)
# anima.name = "ANIMA"
# print(anima)

# child class


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "Cat name: "+str(self.name)+": "+str(self.age)


billy = Cat(12)
billy.name = "Billy"
billy.speak()
print(billy)

johny = Cat(12)
johny.name = "johny"
johny.speak()
print(johny)
