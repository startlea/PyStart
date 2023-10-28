#Zdefiniowanie zmiennej
lista = tuple(range(1, 101))
#pierwsze 10 liczb
first_10 = lista[:10]
#ostatnie 10 liczb
last_10 = lista[-10:]
#ostatnie 10 od końca
last_10_back = last_10[::-1]
#wszystkie nieparzyste
odd = lista[::2]
#wszystkie parzyste od największej do najmniejszej
even = lista[::-2]

print(f'First ten numbers: {first_10}')
print(f'Last 10 numbers: {last_10} {last_10_back}')
print(f'All the odd numbers: {odd}')
print(f'All the even numbers from the biggest to the smallest: {even}')