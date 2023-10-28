number_1 = float(input("Give me number 1 "))
number_2 = float(input("Give me number 2 "))
number_3 = float(input("Give me number 3 "))

if number_1 > number_2 and number_1 > number_3:
    print("Number 1 is the biggest")
elif number_2 > number_1 and number_2 > number_3:
    print("Number 2 is the biggest")
elif number_3 > number_1 and number_3 > number_2:
    print("Number 3 is the biggest")
else:
    print("Try again")

if number_1 < number_2 and number_1 < number_3:
    print("Number 1 is the smallest")
elif number_2 < number_1 and number_2 < number_3:
    print("Number 2 is the smallest")
elif number_3 < number_1 and number_3 < number_2:
    print("Number 3 is the smallest")
else:
    print("Try again")