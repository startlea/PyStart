numbers = '3', '12', '28', '34', '47', '50', '65', '70',

for number in numbers:
   if int(number) % 4 == 0:
      print(f'Liczby podzielne przez 4: {number}')
   elif int(number) % 5 == 0:
      print(f'Liczby podzielne przez 5: {number}')