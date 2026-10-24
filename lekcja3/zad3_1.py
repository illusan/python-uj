# ZADANIE 3.1
# Czy podany kod jest poprawny składniowo w Pythonie?
# Jeśli nie, to dlaczego?


x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y; 
# kod jest poprawny




for i in "axby": if ord(i) < 100: print (i) 
# kod nie jest poprawny, poniewaz if jest instrukcją złozoną, więc nie moze byc w jednej linjce z petla for



for i in "axby": print (ord(i) if ord(i) < 100 else i) #kod jest poprawny
# kod jest poprawny