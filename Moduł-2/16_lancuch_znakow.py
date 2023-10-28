print('Program podaje numer ASCII przyporządkowany do daneego znaku')
characters = input('Podaj jakieś słowo: ')


char_list = list(characters)
for char in char_list:
    print(char, ord(char))