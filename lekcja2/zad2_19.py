# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. 
# Chcemy zbudować string z trzycyfrowych bloków, gdzie liczby 
# jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

L = [1, 67, 420]
tekst = ""

for i in range(len(L)):
    blok = str(L[i]).zfill(3)
    tekst += blok

print(tekst)