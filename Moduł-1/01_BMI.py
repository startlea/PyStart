print("This program will calculate your BMI\n")
height = float(input("What is your hight in meters?"))
weight = int(input("What is your weight in kilograms?"))

BMI = weight / height ** 2

print(f"Your BMI is: {BMI:.2f}")