# iterables revisited

# przepisac ze slajdu i sprobowac zrozumiec
dic = {"a": 1, "b": 2, "c": 3}
# iterating over keys
print(dir(dic))
for x in dic:
    print(x)

for x in dic.values():
    print(x)

# unpacking iterable
d, c = (5, 6)
print(d, c)

for k, v in dic.items():
    print k, v

# home task
# removing punctuation, lowering
# analyze: a b c d e = 0 1 2 3 4
# from left size -5 -4 -3 -2 -1
# create a loop analyzing each character starting from left side
# compare first character with last character, second with last-but-one and so on
# compare if characters are NOT equal
# F[0]! = t[-i-1]
# t[1]! = t
# comparing t[i] with t[-i-1]
# loop lasts until mid of the loop
# mid = len(tc<t) // 2
# for ch in range (mid)
