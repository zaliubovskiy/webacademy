# Task 2 =================================================================================

# ТЗ: # Найти количество четных чисел в массиве.

# Developer notes: Испльзуйте for

# Входные данные:
# input_list = [1, 54, 23, 678, 23, 2322, 798, 34, 22, 1, 23, 54, 45, 67]
# ========================================================================================

input_list = [1, 54, 23, 678, 23, 2322, 798, 34, 22, 1, 23, 54, 45, 67]
j = 0  # Empty variable to count Even integers

for i in input_list:
    if i % 2 == 0:
        j += 1
    else:
        continue

print(f"You've got {j} even integers in your list")



# try to remove else block. it will perfform the same :)
