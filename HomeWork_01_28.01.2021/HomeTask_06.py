# Даны три числа. Написать "yes", если среди них есть одинаковые.

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number == second_number or second_number == third_number or third_number == first_number:
    print("Yes")
else:
    print()
