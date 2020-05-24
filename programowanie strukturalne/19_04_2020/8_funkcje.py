def show():
    print("Witaj", end="")
    print("Janusz")


show()


def iloraz(a, b):
    return a/b


print(iloraz(7, 3))
print(iloraz(b=7, a=3))


def wczytajDane(slownik):
    marka = input("Podaj marke samochodu: ")
    model = input("Podaj model samochodu: ")
    pojemnosc = input("Podaj pojemnosc samochodu: ")
    predkoscMax = input("Podaj predkosc maxymalna samochodu: ")

    slownik["marka"] = marka
    slownik["model"] = model
    slownik["pojemnosc"] = pojemnosc
    slownik["predkoscMax"] = predkoscMax


def wypiszDane(slownik):
    print(f"Marka: {slownik['marka']}")
    print(f"Model: {slownik['model']}")
    print(f"Pojemnosc: {slownik['pojemnosc']}")
    print(f"Predkosc maxymalna: {slownik['predkoscMax']}")


samochod = {}
wczytajDane(samochod)
print()
wypiszDane(samochod)

