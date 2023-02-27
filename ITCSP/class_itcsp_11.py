L = [6, 5, 4, 10, 15, 2]
print(L)
L.sort()
print(L)

L = [6, 5, 4, 10, 15, 6]  # count of certain elements
print(L.count(6))

L = [6, 5, 4, 10, 15, 6]  # count of all elements
print(len(L))

# slicing lists
L1 = [1, 2, 3, 4]
print(L1[1])  # 2, we get a number
print(L1[1:3])  # [2,3], we get a list!!!
print(L1[1:2])  # [2], we get a list!!

L1 = [1, 2, 3, ["a", "Jason", "Brown"], "c"]
print(L1[3][1])  # jason

# list methods that belong to class "list" - all methods that belong to class "list"
# print(dir(list))

# if looking for help concerning list methods
# help(list.append)
# help(list.reverse)

# list of functions
# print(dir(__builtins__))

# TUPLES
t1 = ()
t2 = (1, "two", 3, 25)
t3 = ("one",)
print(t3)
t2[0]
# t2[0] = 2  #ERROR, cannot be defined, tuples are not mutable

print(t2[0])  # 1
t5 = (1, "two", 3.25, ("a", "b", "c"))
print(t5[3][1])  # -> b; same syntax as lists

# slicing
t2 = (1, "two", 3.25)
print(t2[1:2])  # ("two",) COMMA IS CRUCIAL

t4 = t2 + t3  # concatenating a tuple creates a new one
print(t4)

# t2 = (1, "two", 3.25)
# t3 = "one"
# t4 = t2 + t3 #error - we cannot add tuples and strings

T = (1, 2, 9, 5)  # ITERATION - definitely(!) gonna be on the final task
sum = 0
for i in T:
    sum += i
print(sum)

T = (1, 2, 9, 5)
sum = 0
for i in range(len(T)):
    sum += T[i]
print(sum)

# DICTIONARIES
# Ana is key, B is value
student_grades = {"Ana": "B", "Katy": "A", "John": "B"}

s_grade = student_grades["Ana"]  # "B"

all_grades = {}  # empty dictionary

# returns No such key = get method
s_grade = student_grades.get("Rob", "No such key")

student_grades["Bob"] = "A"  # adding value to the dictionary
print(student_grades)

student_grades["Ana"] = 3  # changing value
print(student_grades)

# deleting elements in dictionary
del (student_grades["Katy"])
# OR
# returns No such key - the value we tried to delete
s_grade = student_grades.pop("Rob", "No such key")
print(student_grades)
print(s_grade)

print("John" in student_grades)  # returns true if the element indeed belongs

# student_grades.keys()  # returns all the keys
# print(student_grades.keys())  # not a list
# print(list(student_grades.keys()))  # creates list
# for k in student_grades.keys():
#     # print k
# same with .values instead of .keys

print(student_grades.items())
print(list(student_grades.items()))
for i in student_grades.items():
    print(i)

for k, v in student_grades.items():
    print(k, v)

print(student_grades)
print(len(student_grades))

student_grades.clear()
print(student_grades)

student_grades = {"Ana": "B", "Katy": "A", "John": "B"}
student_grades_01 = student_grades
print(student_grades_01)

student_grades["Ana"] = "C"
print(student_grades)
print(student_grades_01)  # not a copy of the object, but a reference.
# technically the same object under a different name

# student_grades.copy() #making a copy

data = {
    "key1": {
        "inner_key1": 1,
        "inner_key2": 2
    },
    "key2": {
        "inner_key1": 3,
        "inner_key2": 4
    }
}

value = data.get("key1").get("inner_key1", "KEY NOT FOUND ERROR")
print(value)
