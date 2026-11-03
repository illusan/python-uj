# ZADANIE 4.2
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
# które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika
# o dane, tylko korzystać z argumentów.



def make_ruler(n):
    if n < 0:
        raise ValueError("dlugosc miarki nie moze byc ujemna")
    gora = "|" + "....|" * n
    dol = "0"
    for i in range(1, n + 1):
        dol += str(i).rjust(5)
    return gora + "\n" + dol


def make_grid(rows, cols):
    if rows < 0 or cols < 0:
        raise ValueError("liczba wierszy i kolumn nie moze byc ujemna")
    linia = "+" + "---+" * cols + "\n"
    srodek = "|" + "   |" * cols + "\n"
    wynik = linia
    for i in range(rows):
        wynik += srodek + linia
    return wynik


print("make_ruler:")
print(make_ruler(12))


print("make_grid:")
print(make_grid(2, 4))


assert make_ruler(12) == ("|....|....|....|....|....|....|....|....|....|....|....|....|\n"
                          "0    1    2    3    4    5    6    7    8    9   10   11   12")
assert make_ruler(0) == "|\n0"
assert make_grid(2, 4) == ("+---+---+---+---+\n"
                           "|   |   |   |   |\n"
                           "+---+---+---+---+\n"
                           "|   |   |   |   |\n"
                           "+---+---+---+---+\n")
assert make_grid(1, 1) == "+---+\n|   |\n+---+\n"
