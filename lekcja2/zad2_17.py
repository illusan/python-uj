# Posortować wyrazy ze stringu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().

tekst = "Jeszcze nie posortowany tekst ala ma kota"

slowa = tekst.split()

alfabetycznie = sorted(slowa)
dlugosc = sorted(slowa, key=len)

print(f"Posortowane alfabetycznie: {alfabetycznie}")
print(f"Posortowane wzledem dlugosci: {dlugosc}")