# Podać sposób wyświetlania stringu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

string = "word"
wynik = ""

for i in range(len(string)):
    wynik += string[i] + "_"

print(wynik[:-1])