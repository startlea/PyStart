password = input('Podaj swoje hasło: ')

password_strong = password.replace('a', '@', ), password.replace('s', '$')
change_password = ''.join(password_strong)
print(f'Your new password is: {change_password}')



password = str(input('Przerobię podane przez Ciebie hasło: '))

password = list(password)

for letter in password:
    if 'a' in letter or 'A' in letter:
        change_letter = '@'
        indeks = password.index(letter)
        password[indeks] = change_letter

for letter in password:
    if 's' in letter or 'S' in letter:
        change_letter = '$'
        indeks = password.index(letter)
        password[indeks] = change_letter

change_password = ''.join(password)

print(f'Twoje hasło zostało zmienione: {change_password}')