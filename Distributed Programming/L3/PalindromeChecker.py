def is_palindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False


wrd = input("Enter a word: ")
if is_palindrome(wrd):
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")