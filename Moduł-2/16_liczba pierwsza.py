import math
from math import sqrt

number = int(input('Podaj liczbę: '))
is_prime = True
for divider in range(2, math.ceil(sqrt(number))+1):
    if number % divider == 0:
        is_prime  = False
        break

if is_prime:
    print('Liczba jest pierwsza')
else:
    print('Liczba nie jest pierwsza')