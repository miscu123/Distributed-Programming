def read_until_number():
    character = input("Introduceti caracter: ")
    vector = []
    while character.isalpha():
        vector.append(character)
        character = input("Introduceti caracter: ")

    return vector


res = read_until_number()
print("Eroare! ")
print("Rezultat pana la eroare: ", res)
