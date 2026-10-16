# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć string będący ciągiem cyfr kolejnych liczb z listy L.

L = [67, 20, 69, 2137]

tekst = ""

for i in range(len(L)):
    tekst += str(L[i])

print(f"wynik: {tekst}")