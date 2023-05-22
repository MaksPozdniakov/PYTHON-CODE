# import sys
# sys.argv
#################################
# 01

# L1 = sys.argv
# print(L1)
# #################################
# sentence = sys.argv[1]
# print(len(sentence))
# #################################
# n1 = sys.argv[1]
# n2 = sys.argv[2]

# print(n1*n2) nope

# n1 = float(sys.argv[1])
# n2 = float(sys.argv[2])
# print(n1*n2)

# vowels = 'aeiou'
# word = "Winnepesaukee"
# VowelsCount = 0
# for letter in word:
#     if letter in vowels:
#         VowelsCount += 1
# print("You have", VowelsCount, "vowels in a word", word)


# vowels = 'aeiou'
# word = sys.argv[1]
# VowelsCount = 0
# for letter in word:
#     if letter in vowels:
#         VowelsCount += 1
# print(f"You have {VowelsCount} vowels in the word")


# file input-output

# outfile = open("testfile.txt", "w")

# outFile.read()
# outFile.write()
# outFile.close()

# sample_file = open("testfile.txt")

# sample_file = open(r"C:\Users\Maks Pozdniakov\Documents\UAM\PYTHON CODE\ITCSP\class_pp_08.py")

# # open file stream
# # w - if file does not exist, it will be created
# outFile = open("testfile.txt", "w", encoding="utf-8")
# # write to it
# outFile.write("sometext!\n")
# outFile.write("...and some more\n")
# outFile.close()  # closes live stream


# outFile = open("testfile.txt", "w", encoding="utf-8")
# # write to it
# outFile.write("once more some text!\n")
# outFile.write("...and some more more more more\n")
# outFile.close()  # closes live stream

# # appending to a file
# outFile = open("testfile.txt", "a", encoding="utf-8")
# # write to it
# outFile.write("once more some text!\n")
# outFile.write("...who the hell is edgar\n")
# outFile.close()  # closes live stream

# # opening a file
# inFile = open("testfile.txt", "r", encoding="utf-8")
# stuff = inFile.read()  # read from it
# inFile.close()
# print(stuff)

inFile = open("testfile.txt", "r", encoding="utf-8")
stuff = inFile.read()  # read from it
inFile.close()
lines = stuff.print("\n")  # split into lines #??
# print lines and lenghts
for line in lines:
    print(f"{line}, : {len(line)} characters")
