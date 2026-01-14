def count_words_in_file(filename):
    count = 0
    string = filename.split()
    for word in string:
        count += 1

    return count


with open("input.txt", 'r') as file:
    content = file.read()

out = count_words_in_file(content)
print("Output: ", out)