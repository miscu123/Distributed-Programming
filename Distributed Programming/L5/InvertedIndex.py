def inverted_index(documents):
    index = {}
    i = 0

    for doc in documents:
        for word in doc.lower().split():
            if word not in index:
                index[word] = []
            index[word].append(i)
        i += 1

    return index


docs = []
nr = int(input("Enter number of documents: "))

for j in range(nr):
    docm = input("Enter document: ")
    docs.append(docm)

result = inverted_index(docs)

print(result)