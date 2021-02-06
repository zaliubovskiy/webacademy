# Task 2 =================================================================================

# ТЗ:

# Developer notes: Для выполнения данной задачи используйте циклы.
# У строк есть методы "some_string".strip(), "some_string".lstrip(), "some_string".rstrip()
# они позволяют избавляться от пробелов в строках. Используйте этот инструментарий.
# Можете и спользовать конкатенацию строк.

# Входные данные:
# test_str_1 = "  Hello world   this is   me   "
# test_str_2 = "Hello world   this is   me again   "
# test_str_3 = "      "
# test_str_4 = "   Hello world   this is  not actually me   :)"

# На выходе должно быть:
# test_str_1 = "  Hello world this is me"
# test_str_2 = "Hello world this is me again"
# test_str_3 = "      "
# test_str_4 = "   Hello world this is not actually me :)"
# ========================================================================================

test_str_1 = "   Hello world   this is  not actually me   :)"

if test_str_1.isspace():
    print(test_str_1)  # Check if the string contains whitespaces only. If True -> prints the result and ends.
else:
    string_no_end = test_str_1.rstrip()  # Deleting whitespaces in the end
    split_string = " ".join(string_no_end.split())
    # Converts the string to List and then back to string
    # adding ' ' between every element of the list
    print(split_string)

# SECOND SOLUTION with "for" loop:

test_str_1 = "   Hello world   this is  not actually me   :)"

# for i in test_str_1:
#     if i == " " and test_str_1.isalpha[0:i]:
#         continue
#     elif i == " " and test_str_1[i - 1] == " ":
#         test_str_1[i].replace("")
#     else:
#         continue
#
# print(test_str_1)

# Sorry, it's not finished, I am stuck:(
