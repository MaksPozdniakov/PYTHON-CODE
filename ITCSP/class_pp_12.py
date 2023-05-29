# object oriented programming
import random


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "Cat name: "+str(self.name)+": "+str(self.age)


# jelly = Cat(4)
# jelly.set_name("Jelly")
# # str(jelly)
# # Cat.__str__(jelly)
# print("Hello" + str(jelly))
# print("Hello" + Cat.__str__(jelly))
# # print(jelly)

# animec = Animal(10)
# animec.name = "Animec"
# animec.age = 12
# animec.speak()

# billy = Cat(12)
# billy.name = "Billy"
# billy.speak()
# print(billy)


# class Animal(object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None

#     def __add__(self, other):
#         return self.age + other.age


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(f"{self.name} is {diff} years older than {other.name}")
        else:
            print(f"{self.name} is {-diff} years younger than {other.name}")

    def __str__(self):  # overrides __str__() method from Animal class
        return f"Person name: {self.name}, person age: {self.age}"


class Student(Person):
    def __init__(self, name, age, major=None):
        Person().__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need some sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

    def __str__(self):  # overrides __str__() method from Person class
        return f"Student name: {self.name}, student age: {self.age}"


hillary = Person("Hillary", 25)
print(hillary)
tom = Person("Tom", 32)
print(tom)
hillary.add_friend(tom)
print(hillary.friends)

john = Student("John", 25, "IT Dept")
jack = Student("Jack", 27, "IT Dept")

print(jack)
jack.speak()
