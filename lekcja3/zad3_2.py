# ZADANIE 3.2
# Co jest złego w kodzie:


L = [3, 5, 4] ; L = L.sort()
# kod jest zły, ponieważ sort() sortuje listę w miejscu i zwraca None, więc L = None i tracimy listę

x, y = 1, 2, 3
# kod nie jest poprawny, ponieważ są 3 wartości a tylko 2 zmienne, więc wystąpi ValueError

X = 1, 2, 3 ; X[1] = 4
# kod nie jest poprawny, ponieważ X jest krotką, a krotki nie można zmieniać, więc wystąpi TypeError

X = [1, 2, 3] ; X[3] = 4
# kod nie jest poprawny, ponieważ lista ma indeksy 0, 1, 2, a indeksu 3 nie ma, więc wystąpi IndexError

X = "abc" ; X.append("d")
# kod nie jest poprawny, ponieważ string nie ma metody append (napisów nie można zmieniać), więc wystąpi AttributeError

L = list(map(pow, range(8)))
# kod nie jest poprawny, ponieważ pow potrzebuje dwóch argumentów, a map podaje tylko jeden, więc wystąpi TypeError
