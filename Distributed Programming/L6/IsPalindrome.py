def is_palindrome(sentence):
    if len(sentence) <= 1:
        return True

    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    words = sentence[::-1]

    return words == sentence


sent = input("Enter a sentence: ")
out = is_palindrome(sent)
print(out)