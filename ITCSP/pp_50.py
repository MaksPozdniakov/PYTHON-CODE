L1 = [
    ("Bread", 10),
    ("Butter", 20),
    ("Chocolate dark", 15),
    ("Chocolate white", 17),
    ("Cakes", 19)
]


def get_price_filtered_list(filtering_critetion: int, items: list[tuple[str, int]]) -> list[tuple[str, int]]:


price_filtered = list(map(lambda item: item[1], L1))
print(price_filtered)
