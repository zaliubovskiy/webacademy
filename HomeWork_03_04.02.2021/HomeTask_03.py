# Task 3 =================================================================================

# ТЗ: Определите, каких чисел в массиве больше:
# которые делятся (без остатка) на первый элемент массива или
# которые делятся (без остатка) на последний элемент массива.

# Developer notes: Испльзуйте for

# Входные данные:
# input_list = [3, 54, 23, 678, 15, 2322, 798, 34, 33, 1, 23, 54, 45, 2]
# ========================================================================================

input_list = [3, 54, 23, 678, 15, 2322, 798, 34, 33, 1, 23, 54, 45, 2]
first_number_counter = 0
last_number_counter = 0

for i in input_list:
    if i % input_list[0] == 0:
        first_number_counter += 1
    else:
        continue
for j in input_list:
    if j % input_list[-1] == 0:
        last_number_counter += 1

if first_number_counter > last_number_counter:
    print("The array contains more numbers that are divisible by the first element of the array")
elif first_number_counter < last_number_counter:
    print("The array contains more numbers that are divisible by the last element of the array")
else:
    print("The array contains the same numbers that are divisible by the first element and "
          "which are divisible by the last element of the array")