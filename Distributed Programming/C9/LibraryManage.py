class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.este_imprumutata = False

    def __str__(self):
        status = "Imprumutata" if self.este_imprumutata else "Disponibila"
        return f"{self.titlu} - {self.autor} ({status})"


class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if not carte.este_imprumutata:
            carte.este_imprumutata = True
            self.carti_imprumutate.append(carte)
            print(f"{self.nume} a imprumutat cartea: {carte.titlu}")
        else:
            print(f"Cartea '{carte.titlu}' este deja imprumutata.")

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            carte.este_imprumutata = False
            self.carti_imprumutate.remove(carte)
            print(f"{self.nume} a returnat cartea: {carte.titlu}")
        else:
            print(f"{self.nume} nu are cartea '{carte.titlu}' imprumutata.")


class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)

    def sterge_carte(self, carte):
        if carte in self.carti:
            self.carti.remove(carte)

    def listeaza_carti_disponibile(self):
        print("Carti disponibile in biblioteca:")
        for carte in self.carti:
            if not carte.este_imprumutata:
                print(carte)


biblioteca = Biblioteca()

c1 = Carte("1984", "George Orwell", "ISBN001")
c2 = Carte("Mandrie si prejudecata", "Jane Austen", "ISBN002")
c3 = Carte("Crima si pedeapsa", "Dostoievski", "ISBN003")
c4 = Carte("Morometii", "Marin Preda", "ISBN004")
c5 = Carte("Ion", "Liviu Rebreanu", "ISBN005")

for carte in [c1, c2, c3, c4, c5]:
    biblioteca.adauga_carte(carte)

m1 = MembruBiblioteca("Ana")
m2 = MembruBiblioteca("Mihai")
m3 = MembruBiblioteca("Elena")

biblioteca.listeaza_carti_disponibile()
print()

m1.imprumuta_carte(c1)
m2.imprumuta_carte(c1)
m2.imprumuta_carte(c2)
m3.imprumuta_carte(c3)

print()
biblioteca.listeaza_carti_disponibile()
print()

m1.returneaza_carte(c1)
m2.imprumuta_carte(c1)

print()
biblioteca.listeaza_carti_disponibile()
