def run_length_encoding(sentence):
    if not sentence:
        return ""

    final = ""
    count = 1

    for i in range(1, len(sentence)):
        if sentence[i] == sentence[i - 1]:
            count += 1
        else:
            final += sentence[i - 1] + str(count)
            count = 1

    final += sentence[len(sentence) - 1] + str(count)
    return final


sen = input("Enter sentence: ")
print(run_length_encoding(sen))
