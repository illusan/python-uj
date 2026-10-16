# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w stringu line.

tekst ="stół z powyłamywanymi nogami"
slowa = tekst.split()

najdluzszy_wyraz = ""
dlugosc_wyrazu = 0

for i in range(len(slowa)):
    if len(slowa[i]) > dlugosc_wyrazu:
        najdluzszy_wyraz = slowa[i]
        dlugosc_wyrazu = len(slowa[i])


print(f"Najdluzszy wyraz: {najdluzszy_wyraz}")
print(f"Dlugosc najdluzszego wyrazu: {dlugosc_wyrazu}")