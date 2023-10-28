number = int(input("Input a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("The number is devided by 5 and 11")
elif number % 5 == 0:
    print("The number is devided only by 5")
elif number % 11 == 0:
    print("The number is devided only by 11")
else:
    print("The number is not devided by 5 or 11")