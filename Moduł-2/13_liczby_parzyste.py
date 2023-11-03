numbers  = int(input("Podaj liczbę całkowitą: "))
total = 0
length = 0
multiply = 1
for number in range(2, numbers+1, 2):
    total += number
    length += 1
    multiply *= number
    print(number,  end=',')

print()
print(f'Suma wszystkich liczb to: {total}')
print(f'Średnia wszystkich liczb to: {total / length}')
print(f'Średnia wszystkich liczb to: {total / len(range(2, numbers+1, 2))}')
print(f'Iloczyn wszystkich liczb wynosi: {multiply}')