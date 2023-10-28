print("Give me your grades: ")
grades = int(input()), int(input()), int(input()), int(input()), int(input()),
grades_sort = sorted(grades, reverse=True)
print(f'Your grades are: {grades_sort}')

average = sum(grades) / len(grades)
print(f'Your average is: {average:.2f}')

if average >= 4.75:
    print(f'Your average is {average:.2f} you will have red stripe.')
else:
    print('Try next year')