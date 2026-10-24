# ZADANIE 3.10
# Stworzyć słownik tłumaczący liczby zapisane w systemie
# rzymskim (z literami I, V, X, L, C, D, M jako stringami)
# na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].


print("sposob 1:")
D1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
print(D1)


print("sposob 2:")
D2 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
print(D2)


print("sposob 3:")
D3 = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])
print(D3)


print("sposob 4:")
D4 = dict(zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000]))
print(D4)


print("sposob 5:")
D5 = {}
for klucz, wartosc in zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000]):
    D5[klucz] = wartosc
print(D5)

assert D1 == D2 == D3 == D4 == D5


def roman2int(roman):
    wynik = 0
    for i in range(len(roman)):
        wartosc = D1[roman[i]]
        if i + 1 < len(roman) and D1[roman[i + 1]] > wartosc:
            wynik -= wartosc
        else:
            wynik += wartosc
    return wynik


print("roman2int:")
print("MCMXCIV =", roman2int("MCMXCIV"))

assert roman2int("III") == 3
assert roman2int("IV") == 4
assert roman2int("IX") == 9
assert roman2int("LVIII") == 58
assert roman2int("MCMXCIV") == 1994
assert roman2int("MMXXVI") == 2026
