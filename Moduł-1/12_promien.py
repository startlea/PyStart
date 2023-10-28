from math import pi
from math import sqrt
#The length of your section
xa = int(input("Give me point xa: "))
ya = int(input("Give me point ya: "))
xb = int(input("Give me point xb: "))
yb = int(input("Give me point yb: "))

a = float(sqrt((xb - xa)**2 + (yb - ya)**2))

print(f"The length of your section is  {a:.2f}")

#Coordinates of the center of the diagonal
point_s_1 = (xa+xb)/2
point_s_2 = (ya+yb)/2

print(f"The middle of your section is at the point: {point_s_1}, {point_s_2}")

#Area and radius of a circle
circle_area = pi * sqrt(a/2)
radius = a/2

print(f"The area of your circle is: {circle_area:.2f}")
print(f"The radius of your circle is: {radius:.2f}")

#Bases, area and perimeter of your rectangle
base_a = sqrt((xb - xa) ** 2)
base_b = sqrt((yb - ya) ** 2)
rect_area = base_b * base_a
perimeter  = 2 * base_a + 2 * base_b
print(f"The base a is {base_a} and base b {base_b}")
print(f"Rectangle area is {rect_area:.2f}")
print(f"The perimeter of the rectangle is {perimeter:.2f}")
