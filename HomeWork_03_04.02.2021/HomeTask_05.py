# Task 5 =================================================================================

# ТЗ: # Дан массив. Сформировать новый массив,
# в котором идут сначала отрицательные элементы, затем нули, затем положительные.

# Developer notes: Испльзуйте for

# Входные данные:
# input_list = [23, 65, 23, 0, 234, 0, -12, 0, 740, -13, -409, 0]
# ========================================================================================

input_list = [23, 65, 23, 0, 234, 0, -12, 0, 740, -13, -409, 0]
# Obvious solution: print(input_list.sort())

negative_numbers = []
zeros = []
positive_numbers = []

for i in input_list:
    if i < 0:
        negative_numbers.append(i)
    elif i > 0:
        positive_numbers.append(i)
    else:
        zeros.append(i)

sorted_list = negative_numbers + zeros + positive_numbers
print(sorted_list)
