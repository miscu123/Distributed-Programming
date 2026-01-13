def reverse_words(sentence):
    words = sentence.split()
    words.reverse()

    sen = ""
    for word in words:
        sen += word + " "

    return sen


sent = input("Enter a sentence: ")
print(reverse_words(sent))