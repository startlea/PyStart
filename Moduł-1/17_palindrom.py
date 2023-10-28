number = str(input("Give me a number: "))
reversed_number = number[::-1]
print(reversed_number)

if number == reversed_number:
    print("The number is palindromic")
else:
    print("The number is not palindromic")