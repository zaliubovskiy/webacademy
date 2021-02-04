# Дано два числа. Вывести yes, если они отличаются на 100, иначе вывести No.

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

difference = first_number - second_number

if difference == 100 or difference == -100:  # this way, we include both options, "a > b" and "a < b".
    print("Yes")
else:
    print("No")
