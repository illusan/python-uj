# Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line. 
# Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line.

tekst = "Chce zdac metody numeryczne"
slowa = tekst.split()
wynik = ""

for i in range(len(slowa)):
    wynik += slowa[i][-1]

print(wynik)