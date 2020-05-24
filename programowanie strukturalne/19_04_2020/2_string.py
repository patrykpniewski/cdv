text = "Anna, pawel, TomEK"

tab = text.split(", ")
print(tab)

name = "Janusz"
nameUpper = name.upper()

print(nameUpper)

nameLower = name.lower()

print(nameLower)

# surname = input("Podaj swoje nazwisko: ")
# content = surname.isalpha()

# print(content)

text1 = "Jan\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + " " + text2)

# wyswietlanie łancuchów znaków

text = "%s %s" % ("PHP", "Python")
print(text)

text = "{1} {0}".format("PHP", "Python")
print(text)

# help(text.replace)

new = text.replace("PHP", "C#")
print(new)

year = 2020
month = "MAY"
day = 24
print("Data: ", end="")
print(day, month, year, sep="-")
