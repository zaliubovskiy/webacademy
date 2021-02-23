# Task 1 =================================================================================

# ТЗ: Сформировать массив из элементов арифметической прогрессии
# с заданным первым элементом x и разностью d.

# Developer notes: Испльзуйте range() и for

# Входные данные:
# длинна массива = 47
# x = 4
# d = 2
# ========================================================================================

a = 47  # List length
x = 4  # First element
d = 2  # Difference between numbers
list_arithmetic = []

for i in range(a):
    list_arithmetic.append(x)
    x += d

print(list_arithmetic)  # There was nothing about printing in a Task, need to check if it's needed!


# Good one. But try to use range(x, y, z) parameters for that. You are usinf FOR here but never used i itself in it.
