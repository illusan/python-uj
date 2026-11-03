# ZADANIE 4.5
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście
# od numeru left do right włącznie. Lista jest modyfikowana w miejscu (in place).
# Rozważyć wersję iteracyjną i rekurencyjną.


def sprawdz_indeksy(L, left, right):
    if left < 0 or right >= len(L) or left > right:
        raise ValueError("nieprawidlowe indeksy left i right")


def odwracanie(L, left, right):
    sprawdz_indeksy(L, left, right)
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rek(L, left, right):
    sprawdz_indeksy(L, left, right)

    def odwroc(left, right):
        if left < right:
            L[left], L[right] = L[right], L[left]
            odwroc(left + 1, right - 1)

    odwroc(left, right)


print("wersja iteracyjna:")
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odwracanie(L, 2, 6)
print(L)


print("wersja rekurencyjna:")
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odwracanie_rek(L, 2, 6)
print(L)


for funkcja in (odwracanie, odwracanie_rek):
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    funkcja(L, 2, 6)
    assert L == [0, 1, 6, 5, 4, 3, 2, 7, 8, 9]

    L = [1, 2, 3, 4]
    funkcja(L, 0, 3)
    assert L == [4, 3, 2, 1]

    L = [1, 2, 3]
    funkcja(L, 1, 1)
    assert L == [1, 2, 3]
