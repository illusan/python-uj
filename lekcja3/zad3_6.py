# ZADANIE 3.6
# Napisać program rysujący prostokąt zbudowany z małych kratek.
# Należy zbudować pełny string, a potem go wypisać.
# Liczby kratek w wierszach (y) i kolumnach (x) mają być zapisane
# w osobnych zmiennych jako parametry programu.
# Przykładowy prostokąt składający się 2 × 4 pól ma postać:
#
# +---+---+---+---+   (x = 4, y = 2)
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+


x = 4
y = 2

linia = "+" + "---+" * x + "\n"
srodek = "|" + "   |" * x + "\n"

prostokat = linia
for i in range(y):
    prostokat += srodek + linia

print(prostokat)

assert prostokat == ("+---+---+---+---+\n"
                     "|   |   |   |   |\n"
                     "+---+---+---+---+\n"
                     "|   |   |   |   |\n"
                     "+---+---+---+---+\n")
