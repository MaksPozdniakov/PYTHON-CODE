# REGULAR EXPRESSIONS #regex

import re
import sys

# if re.search("^a[b-e]", sys.argv[1]):
#     print("a match")
# else:
#     print("no match")

# if re.search("[b-e]a$", sys.argv[1]):
#     print("a match")
# else:
#     print("no match")

# if re.search("[a-zA-Z]a$", sys.argv[1]):  # returns any word that ends with a, big and small
#     print("a match")
# else:
#     print("no match")

# returns any word that ends with a, big and small even bettttter
# if re.search("[a-zA-Z][aA]$", sys.argv[1]):
#     print("a match")
# else:
#     print("no match")

# if re.search("[a-z]ana$", sys.argv[1]):
#     print("a match")
# else:
#     print("no match")

# if re.search("[a-z]/s$", sys.argv[1]):
#     print("a match")
# else:
#     print("no match")

# if re.search("he*o", sys.argv[1]): #zero or any occurencies of e
#     print("a match")
# else:
#     print("no match")

# if re.search("h^e*o", sys.argv[1]): #zero or any occurencies of e
#     print("a match")
# else:
#     print("no match")

# h and e are obligatory, o should be the last one
# if re.search("he.*o", sys.argv[1]):  # zero or many characters and o in the end
#     print("a match")
# else:
#     print("no match")

# if re.search("he[a-cA-C*o", sys.argv[1]):  # zero or many characters and o in the end
#     print("a match")
# else:
#     print("no match")

# l_txt = [
#     "hello world",
#     "gghello world",
#     "hello world and planet"
# ]
# for text in l_txt:
#     x = re.search("he.*o", text)
#     print(text + "-->" + str(x))

# findall() function - returns all the matches
# find list of instances: banana

# txt = "This is sbananaes. Banana is good. banana."
# # L1 = re.findall("banana", txt)
# # L1 = re.findall("banana", txt.lower())
# L1 = re.findall("[Bb]anana", txt)
# print(L1)

# split() function - returns a list where the string has been split at each match
# white space - space, tab, enter, etc. (horizontal and vertical)

txt = "This is sbananaes. Banana is good. banana."
L1 = re.split("\s", txt)
print(L1)
