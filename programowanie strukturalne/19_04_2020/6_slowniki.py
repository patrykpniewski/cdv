pracownik = {
    "imie": "Patryk",
    "nazwisko": "Pniewski",
    "miasto": "Poznań",
    "wiek": 20,
    "imionaDzieci": ["Brajanek", "Seba"],
    "imionaRodzicow": ["Karyna", "Janusz"],
}

print(f"Dziecko 1: {pracownik['imionaDzieci'][0]}")
print(f"Dziecko 2: {pracownik['imionaDzieci'][1]}")

pracownik['wzrost'] = 180
pracownik['waga'] = 80
print(pracownik)

key = "wiek"
if key in pracownik:
    del pracownik[key]
    print(f"Klucz o nazwie {key} został usunięty")

print(pracownik.values())
print(pracownik.items())
print()

for key, value in pracownik.items():
    print(f"{key}: {value}")
