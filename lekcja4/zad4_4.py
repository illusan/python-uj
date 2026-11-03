# ZADANIE 4.4
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.


def fibonacci(n):
    if n < 0:
        raise ValueError("numer wyrazu nie moze byc ujemny")
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print("fibonacci(10) =", fibonacci(10))


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(10) == 55
assert [fibonacci(i) for i in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
