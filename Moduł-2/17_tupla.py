list = tuple(range(12, 1024, 6))
#average = sum(grades) / len(grades)

for tuple in list:
 print(tuple)
print('Liczb w tupli jest ', (len(range(12, 1025, 6))))
print('Pierwsze trzy liczby to: ', list[:3])
print('Przedostatnia liczba to: ', list[-2::2])
print('Co szósty element licząc od czwartego to: ', list[3::6])
print('Liczb w tupli jest ', list[::-3])
print('Średnia ostatnich 10 wartości wynosi: ', sum(list[-10::]) / len(list[-10::]) )