# ZADANIE 3.5
# Napisać program rysujący "miarkę" o zadanej długości.
# Długość miarki (x) ma być zapisana w osobnej zmiennej jako parametr programu.
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
# (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
# Należy zbudować pełny string, a potem go wypisać.
#
# |....|....|....|....|....|....|....|....|....|....|....|....|   (x = 12)
# 0    1    2    3    4    5    6    7    8    9   10   11   12


x = 12

gora = "|" + "....|" * x
dol = "0"
for i in range(1, x + 1):
    dol += str(i).rjust(5)

miarka = gora + "\n" + dol
print(miarka)

assert miarka == ("|....|....|....|....|....|....|....|....|....|....|....|....|\n"
                  "0    1    2    3    4    5    6    7    8    9   10   11   12")
