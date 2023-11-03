number = float(input('Podaj liczbę: '))
print(f'Liczba {number} podniesiona do potęgi 2, 3, 4 i 5 to kolejno ')
for power in range(2, 6):
    print(f'{float(number ** power):.2f}', end=', ')