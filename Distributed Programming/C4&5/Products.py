preturi_produse = {}
stocuri = {}

numar_produse = int(input("Introdu nr de produse: "))

for i in range(numar_produse):
    print(f"\nProdusul {i + 1}:")
    nume = input("Nume produs: ")
    pret = float(input("Pret produs: "))
    stoc = int(input("Stoc initial: "))

    preturi_produse[nume] = pret
    stocuri[nume] = stoc

vanzari = []
numar_vanzari = int(input("\nIntrodu nr de vanzari din zi: "))

for i in range(numar_vanzari):
    print(f"\nVanzarea {i + 1}:")
    produs = input("Nume produs vandut: ")
    cantitate = int(input("Cantitate vanduta: "))
    vanzari.append((produs, cantitate))

venit_total = 0.0
raport_erori = []

for produs, cantitate in vanzari:
    if produs not in preturi_produse:
        raport_erori.append(f"Produs inexistent: {produs}")
        continue

    if stocuri[produs] < cantitate:
        raport_erori.append(
            f"Stoc insuficient pentru {produs} (disponibil: {stocuri[produs]}, cerut: {cantitate})"
        )
        continue

    venit_total += preturi_produse[produs] * cantitate
    stocuri[produs] -= cantitate

produse_de_realimentat = {
    produs for produs, cantitate in stocuri.items() if cantitate < 5
}

raport = []
raport.append(f"Venit total: {venit_total:.2f} RON\n")
raport.append("Stocuri ramase:\n")

for produs, cantitate in stocuri.items():
    raport.append(f"  - {produs}: {cantitate}\n")

raport.append("\nProduse ce pentru realimentare:\n")
for produs in produse_de_realimentat:
    raport.append(f"  - {produs}\n")

if raport_erori:
    raport.append("\nErori:\n")
    for eroare in raport_erori:
        raport.append(f"  - {eroare}\n")

print("\n===== RAPORT ZILNIC =====")
for linie in raport:
    print(linie, end="")

with open("raport_stocuri.txt", "w", encoding="utf-8") as fisier:
    fisier.writelines(raport)

print("\n\nRaportul salvat")