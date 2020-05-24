def div(x, y):
    try:
        return round(x/y, 2)
    except ZeroDivisionError:
        print("Nie dziel przez 0!")


res = div(2, 3)
print(res)

# Użytkownik podaje wartość z klawiatury do momentu wpisania liczby całkowitej
# wykorzystaj pętlę while i wyjątek


while 1:
    try:
        x = input("Podaj liczbę całkowitą: ")
        x = int(x)
        break
    except ValueError:
        print("Nie podałeś liczby całkowitej")
    finally:
        print("Koniec pętli")

print(f"Podana wartość to: {x}")
