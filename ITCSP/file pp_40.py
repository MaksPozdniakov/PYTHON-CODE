'''
Exercise 40, pp_30.py

Task is the same as in exercise 30 but additionally you have to write & use a function removing punctuation.
Write a program with a function called map_longest() that takes a text as a parameter and returns the longest word contained in that text and its length - tuple.

Result of a program should be a message 
e.g.,
The longest word in the text is 'decision-making.' with the length of 16 characters

use map function together with lambda, don't deal with punctuation
'''
from string import punctuation
# import string


def remove_punctuation(word: str) -> str:
    '''
    Function removes punctuation from the given string

    Parameters:
        word: any string with or without the punctuation
    Returns:
        string without punctuation
    '''
    r: str = str()
    for letter in word:
        if letter in punctuation:
            continue
        r += letter
    return r

    # text_clean = word.translate(str.maketrans('', '', string.punctuation))
    # text_clean = text_clean.lower()
    # return text_clean


def map_longest(text: str) -> tuple:
    '''
    Function returns the longest word in the text and it's length

    Parameters:
        text: any text

    Returns:
        tuple: a tuple containing the longest word and it's length

    '''
    text_split = text.lower().split()
    text_tuples: list[tuple[str, int]] = list(
        map(lambda x: (x, len(x)), text_split))
    text_tuples.sort(key=lambda x: x[1], reverse=True)
    return text_tuples[0]

    # word_list = text.split()
    # longest = max(word_list, key=len)
    # tup = (longest, len(longest))
    # return tup


text = '''
Artificial Intelligence (AI) is a rapidly evolving field that involves the development of computer systems capable of performing tasks that typically require human intelligence such as 
visual perception, speech recognition, and decision-making. AI systems can be trained using large amounts of data to recognize patterns and make predictions. Machine learning is a 
subfield of AI that focuses on the development of algorithms that can learn from and make predictions based on data. The use of AI is becoming widespread across various industries, 
including healthcare, finance, transportation, and retail. While AI has the potential to bring about significant positive change in our society, it also raises ethical and social issues. 
For example, the use of AI in decision-making could perpetuate existing biases and lead to unfair outcomes. There are also concerns about job displacement as AI systems become more capable 
of performing tasks that were previously done by humans. To address these challenges, there is a growing need for responsible and ethical AI development and deployment. 
This involves creating systems that are transparent, explainable, and accountable, as well as investing in education and training to ensure that individuals have the skills and knowledge 
to participate in the AI-driven economy. In conclusion, AI is a rapidly evolving field that has the potential to bring about significant positive change, but it is important that we approach 
its development and deployment with caution and responsibility.
'''
result: tuple[str, int] = map_longest(remove_punctuation(text))
print(
    "The longest word in the text is"
    f" '{result[0]}' with the length of {result[1]} characters."
)

# text_clean = remove_punctuation(text)
# result = map_longest(text_clean)
# print(
#     f"The longest word in the text is '{result[0]}' with the length of {result[1]} characters")
