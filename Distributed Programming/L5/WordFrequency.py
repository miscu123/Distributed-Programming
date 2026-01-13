from collections import Counter


def word_frequency(text):
    text = text.lower()
    words = text.split()
    freq_map = Counter(words)
    print(dict(freq_map))


st = input("Enter a string: ")
word_frequency(st)
