# ZADANIE 4.6
# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji,
# która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną,
# a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).


def sum_seq(sequence):
    suma = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            suma += sum_seq(item)
        else:
            suma += item
    return suma


sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("sum_seq =", sum_seq(sequence))


assert sum_seq(sequence) == 45
assert sum_seq([]) == 0
assert sum_seq([[[[]]]]) == 0
assert sum_seq([1, 2, 3]) == 6
assert sum_seq((1.5, [2.5, (3,)])) == 7.0
