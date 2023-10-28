import datetime

x = datetime.datetime.now()
print(x.strftime("%c"))

#User age
birth_year = int(input("What year were you born? "))
current_datetime = datetime.datetime.now()
year_now = current_datetime.year
age  = year_now - birth_year

print(f"Thank you, you are {age} years old")

#Conditional statement
if age >= 18:
    print("You are of legal age!")
else:
    print("You are under 18, I can't let you in, come back when you turn 18")

if birth_year % 4 == 0 or birth_year % 100 == 0 or birth_year % 400 == 0:
    print("The year of birth was a leap year")
else:
    print("The year of birth was not a leap year")