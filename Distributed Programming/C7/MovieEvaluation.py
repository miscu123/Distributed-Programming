with open("movies.txt", 'r') as file:
    movies = file.readlines()

while True:
    print("--------------------------------------")
    print("Alege o optiune:")
    print("1. Vizualizeaza filmele si evaluarile")
    print("2. Adauga un nou film cu evaluare")
    print("3. Actualizeaza evaluarea unui film")
    print("4. Sterge un film")
    print("5. Salveaza modificarile si iesi")

    opt = input("--> ")

    if opt == "1":
        for movie in movies:
            print(movie.strip())
    elif opt == "2":
        titlu = input("Titlu film: ")
        evaluare = input("Evaluare: ")
        movies.append(titlu + ", " + str(evaluare) + "\n")
    elif opt == "3":
        titlu = input("Introdu titlul filmului: ")
        for i, movie in enumerate(movies):
            if movie.lower().startswith(titlu.lower()):
                evaluare = input("Noua evaluare: ")
                movies[i] = titlu + ", " + str(evaluare) + "\n"
                break
        else:
            print("Filmul nu a fost gasit.")
    elif opt == "4":
        titlu = input("Introdu titlul filmului de sters: ")
        found = False
        new_movies = []

        for m in movies:
            if m.lower().startswith(titlu.lower()):
                found = True
            else:
                new_movies.append(m)

        if found:
            movies = new_movies
            print("Filmul a fost sters.")
        else:
            print("Filmul nu a fost gasit.")
    elif opt == "5":
        with open("movies.txt", "w") as file:
            file.writelines(movies)
        print("Modificarile au fost salvate.")
        break
    else:
        print("Optiune invalida.")