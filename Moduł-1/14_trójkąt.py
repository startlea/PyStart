from math import sqrt

a = float(input("Give the triangle side "))

area = (a** 2 * sqrt(3))/4
perimeter = 3 * a
print(f"Area of the triangle is: {area:.2f}")
print(f"Perimeter of the triangle is: {perimeter:.2f}")