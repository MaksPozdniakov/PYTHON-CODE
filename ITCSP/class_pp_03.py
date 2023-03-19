# filtering a simple collection

# L1 = [1, 2, 4, 2, 9, 11, 12]


# def filter_list(item):
#     return item > 10


# filtered_list = list(filter(filter_list, L1))
# print(filtered_list)
# print("--------------------")

# more complex data structure

# L1 = [
#     ("Bread", 10),
#     ("Butter", 20),
#     ("Chocolate dark", 15),
#     ("Chocolate white", 17),
#     ("Cakes", 19)
# ]


# def price_filter(item):
#     return item[1] > 15


# filtered_list = list(filter(price_filter, L1))
# print(filtered_list)
# print("--------------------")


# L1 = [
#     ("Bread", 10),
#     ("Butter", 20),
#     ("Chocolate dark", 15),
#     ("Chocolate white", 17),
#     ("Cakes", 19)
# ]

# criteria = 15
# filtered_list = list(filter(lambda item: item[1] > criteria, L1))
# print(filtered_list)

# #for dictionaries:
# filtered_list = list(filter(lambda item: item["Price"] > 15, L1))
# print(filtered_list)

# LIST REVISITED

# words = ["data", "science", "machine", "learning"]
# word_length = []
# for word in words:
#     word_length.append(len(word))
# print(word_length)

# word_length = list(map(lambda item: len(item), words))

# word_length = [len(x) for x in words]
# print(word_length)

# LIST COMPREHENSION
# one line command, a new list is created

# word_length = [len(word) for word in words]
# print(word_length)

# print("--------------------")

# L1 = [
#     ("Bread", 10),
#     ("Butter", 20),
#     ("Chocolate dark", 15),
#     ("Chocolate white", 17),
#     ("Cakes", 19)
# ]

# prices = [item[1] for item in L1]
# print(prices)

# print("--------------------")

# L1 = [
#     ("Bread", 10),
#     ("Butter", 20),
#     ("Chocolate dark", 15),
#     ("Chocolate white", 17),
#     ("Cakes", 19)
# ]

# prices only
# prices = [item[1]*1.2 for item in L1]
# print(prices)
# product together with prices
# in list comprehension we create tuples with ()
# product_prices = [(item[0], item[1]*1.2) for item in L1]
# print(product_prices)

# print("--------------------")

# L1 = [
#     ("Bread", 10),
#     ("Butter", 20),
#     ("Chocolate dark", 15),
#     ("Chocolate white", 17),
#     ("Cakes", 19)
# ]

# first filter, then increase the price
# prices = [(item[0], item[1]*1.2) for item in L1 if item[1] > 15]
# print(prices)

# DICTIONARY REVISITED

# standard way of creating a dictionary
# words = ["data", "science", "machine", "learning"]
# word_length = {}
# for word in words:
#     word_length[word] = len(word)
# print(word_length)

# shakespeare text length analyzer
# work with "chaining"

# dictionary supreme
# shakespeare = "When forty winters shall besiege thy brow, And sig deep trenches in the beautys field, ..."
# shakespeare = shakespeare.replace(",", "").replace(".", "")
# words = shakespeare.split()
# word_length = {}
# for word in words:
#     word_length[word] = len(word)
# print(word_length)

# print("--------------------")

# DICTIONARY COMPREHENSION

# words = ["data", "science", "machine", "learning"]
# word_length = {word: len(word) for word in words}
# print(word_length)

# new dictionary from a dictionary - dict.items() {key: value for (key, value) in dict.items()}

# shakespeare = "When forty winters shall besiege thy brow, And sig deep trenches in the beautys field, ..."
# words = shakespeare.replace(",", "").replace(".", "").split()
# word_length = {word: len(word) for word in words}
# print(word_length)

# dicitionary of words instead of a list

# product_price_dic = {
#     ("Bread", 10),
#     ("Butter", 20),
#     ("Chocolate dark", 15),
#     ("Chocolate white", 17),
#     ("Cakes", 19)
# }

# # new dictionary - items()
# product_price_increased = {k: v*1.2 for k, v in product_price_dic.items()}
# print(product_price_increased)


# shakespeare = "When forty winters shall besiege thy brow, And sig deep trenches in the beautys field, ..."
# words = shakespeare.replace(",", "").replace(".", "").split()
# word_length = {word: len(word) for word in words}
# sorted_word_length = sorted(
#     word_length.items(), key=lambda item: item[1], reverse=True)
# print(sorted_word_length)
# print(dict(word_length))  # normally 'sorted' returns list
