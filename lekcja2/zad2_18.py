# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na string.

liczba = 2137067
tekst = str(liczba)
licznik = 0

for i in range(len(tekst)):
    if tekst[i] == "0":
        licznik += 1

print(f"Liczba cyfr zero: {licznik}")