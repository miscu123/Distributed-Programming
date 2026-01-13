# Am ales sa repet introducerea parolelor astfel (prin while), pentru un aspect mai placut si pentru o verificare a parolei introduse imediat dupa enter.
# In cazul in care dorim iesirea din program pur si simplu nu introducem niciun caracter
# Initial in criteria consider parola total gresita, iar parcurgand string-ul se verifica corectitudinea ei

def check_password(password):
    criteria = ['Prea putine caractere!', 'Lipseste caracter majuscul!', 'Lipseste caractere minuscul!', 'Lipseste numar!', 'Lipseste caracter special!', '0']
    err = 0

    for char in password:
        if len(password) >= 8:
            criteria[0] = '0'
        elif char.isupper():
            criteria[1] = '0'
        elif char.islower():
            criteria[2] = '0'
        elif char.isdigit():
            criteria[3] = '0'
        elif char in '!@#$%^&*()-_+=<>?':
            criteria[4] = '0'
        elif char == ' ':
            criteria[5] = "Contine spatiu!"

    for char in criteria:
        if char != '0':
            if err == 0:
                print("Parola dvs. este slaba.")
                err += 1
            print(char)

    if err == 0:
        print("Parola dvs. este puternica!")

    print("---------------------------")


def main():
    psw = 'intro'
    while psw != '':
        psw = input("Introduceti parola: ")
        if psw == '':
            print("Iesire din program!")
            break
        check_password(psw)


main()