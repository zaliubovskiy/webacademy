# Task 1 =================================================================================

# ТЗ: Дано четырехзначное число. Верно ли, что цифры в нем расположены по убыванию?
# Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да.

# Developer notes: В Python число можно "превратить" в строку с помощью функции str()
# Строку можно итерировать циклом FOR. Используйте его.
# ========================================================================================

input_number = int(input("Please enter the 4-digit number: "))
input_string = str(input_number)  # converted into str, in order to use the "for" loop.
j = 1  # index of the i+1, in order to compare i and i+1.

for i in input_string:
    if i > input_string[j] and j == 3:
        print("Yes")
        break
    elif i > input_string[j]:
        j += 1
        continue
    else:
        print("No")
        break

# Is this a problem that I resolved it without "enumerate" function?
# No, no at all. Noce one.
# But why are converting input in int() and then in str() again?
# If you need string in code after input() just don't convert it to int()


# FIRST OBVIOUS SOLUTION
# --------------------------------------------------------------

# input_number = int(input("Please enter the 4-digit number: "))
# input_string = str(input_number)

# if input_string[0] > input_string[1] > input_string[2] > input_string[3]:
#     print("Yes")
# else:
#     print("No")
