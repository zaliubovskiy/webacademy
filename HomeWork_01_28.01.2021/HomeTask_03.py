# Пользователь вводит номер месяца, вывести название месяца. (попробуйте решить с применением цикла)

month_number = int(input("Please enter the number of the month (enter '0' to exit): "))

if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")
else:
    print("Please enter a valid month number (from 1 to 12): ")
