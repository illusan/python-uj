# ZADANIE 3.8
# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).


seq1 = [1, 2, 3, 3, 4, 5]
seq2 = (4, 5, 5, 6, 7)


print("(a) elementy wystepujace w obu sekwencjach:")
wspolne = list(set(seq1) & set(seq2))
print(wspolne)


print("(b) wszystkie elementy z obu sekwencji:")
wszystkie = list(set(seq1) | set(seq2))
print(wszystkie)


assert sorted(wspolne) == [4, 5]
assert sorted(wszystkie) == [1, 2, 3, 4, 5, 6, 7]
assert sorted(set("abcd") & set("cdef")) == ["c", "d"]
assert sorted(set("abcd") | set("cdef")) == ["a", "b", "c", "d", "e", "f"]
