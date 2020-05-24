"""
[] Lista
() Tuple
{} Słowniki
"""

progr = ["Python", "PHP", "C#", "Java"]
print(progr)
print(type(progr))

first = progr[0]
print(first)

threeElements = progr[:3]
print(threeElements)

lastElement = progr[-1]
print(lastElement)

progr.append("R")
progr.append("Python")
print(progr)

countElements = progr.count("Python")
print(countElements)

countElementsOfList = len(progr)
print(f"Ilość elementów w liście: {countElementsOfList}")

# połączenie list
anotherList = ["C", "C++"]

progr.extend(anotherList)
print(progr)
print(anotherList)

new = progr
new.clear()
print(f"Lista: progr: {progr}")
print(f"Lista: new: {new}")
