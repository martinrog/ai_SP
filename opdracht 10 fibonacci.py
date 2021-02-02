# Opdracht 10 - Fibonaci
# De rij begint met 0 en 1 en vervolgens is elk volgende element van de rij steeds de som van de twee voorgaande elementen.
# Bij de rij gebruiken we de notatie fn voor het aangeven van het n-de element van de rij. f9 is
# bijvoorbeeld gelijk aan 34. De eerste elementen van de rij zijn dan als volgt:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584
# Implementeer een functie die fn uitrekent gegeven integer n. De functie moet recursief zijn.
#

l = [0, 1]

def fibo(n, v1=0, v2=1):
    if n > 0:
        return fibo(n-1, v2, v1+v2)
    # else:
    #     return fibo(v1,v2)[n]

fibo(9)