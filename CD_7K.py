"""Задача_7Ku с CodeWars"""
import re
from collections import Counter

def top_3_words(text):
    # Convert the text to lowercase
    text = text.lower()
    # Replace any characters that are not letters or apostrophes with whitespace
    text = re.sub("[^a-z']+", ' ', text)

    # Split the text into individual words
    words = text.split()

    # Count the occurrences of each word
    word_count = Counter(words)
    # Get the top 3 most occurring words
    top_words = word_count.most_common(3)

    # Extract only the words (ignoring the counts)

    top_words = [word for word, _ in top_words]


    top_words = ([x for x in top_words if " ".join(set(x)) != "'"])
    str(top_words).replace("'", '"')
    return top_words


s= "   //wont won't won't  aa aa '''"
print(top_3_words(s))
