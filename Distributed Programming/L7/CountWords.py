def count_words_in_file(filename):
    string = filename.split()

    return len(string)


with open("input.txt", 'r') as file:
    content = file.read()

out = count_words_in_file(content)
print("Output: ", out)