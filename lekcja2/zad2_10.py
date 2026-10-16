# Mamy dany string wielowierszowy line. 
# Podać sposób obliczenia liczby wyrazów w stringu. 
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

tekst = "Ala ma kota"

slowa = tekst.split()

licznik = len(slowa)

print(f"Podany tekst ma {licznik} wyrazów")
