password = input('Podaj swoje hasło: ')

password_strong = password.replace('a', '@', ), password.replace('s', '$')

print(f'Your new password is: {password_strong}')