# Znaleźć łączną długość wyrazów w stringu line. Wskazówka: można skorzystać z funkcji sum().

tekst = "Bardzo przyjemne zadania, pozdrawiam"
suma = 0

slowa = tekst.split()
for i in range(len(slowa)):
    suma += len(slowa[i])


print(f"laczna dlugosc wyrazow: {suma}")