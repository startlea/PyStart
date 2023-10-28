sentence = '12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek'
total = 0
for word in sentence.split(' '):
    if word.isnumeric():
 #       total = total + int(word)
        total += int(word)
print(f'Łączna waga produktów wynosi {total}kg')