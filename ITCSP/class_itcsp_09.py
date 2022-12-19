import string
print("hat" == "hat")
print("Hat" == "hat")
print("Hat" > "hat")
print("h" > "cat")


print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

print(ord("H"))
print(ord("h"))
print(ord("c"))
print(ord("ł"))
print(ord("l"))

x = isinstance(5, int)
print(x)

number = 5
if isinstance(number, int):
    print("Yes")
else:
    print("NO")

number = 5.0
print("Yes") if isinstance(number, int) else print("No")

s = "Hi there"
print(s.upper())
print(s)
s2 = s.lower()
print(s2)

s = "Hi there"
print(s.capitalize())
print(s)
s2 = s.capitalize()
print(s2)

s = "he lives in poznan"
print(s.title())
print(s)
s2 = s.title()
print(s2)

s = "           he lives in poznan          "
print(s.strip())
print(s)
s2 = s.strip()
print(s2)

s = "he lives in poznan"
print(s.strip("n"))
print(s)
s2 = s.strip("n")
print(s2)

s = "he lives in poznan"
print(s.find("i"))
print(s.find("b"))

s = "he lives in poznan"
print(s.index("i"))
print(s.index("b"))

s = "he lives in poznan"
print(s.replace("i", "B"))
print(s.replace("i", "b", 1))
print(s.replace("i", ""))  # removing all i's
