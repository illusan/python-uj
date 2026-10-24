# ZADANIE 3.4
# Napisać program pobierający w pętli od użytkownika
# liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x.
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
# Jeżeli użytkownik wpisze napis zamiast liczby, to program
# ma wypisać komunikat o błędzie i kontynuować pracę.


while True:
    tekst = input("Podaj liczbę (stop kończy program): ")
    if tekst == "stop":
        break
    try:
        x = float(tekst)
    except ValueError:
        print("Błąd: to nie jest liczba!")
        continue
    print(x, x ** 3)
