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

# check this out:
# def zipper(test_string):
#     result_string = ""
#     flag_1 = False
#     flag_2 = False
#     for i in test_string:
#         if i == " " and not flag_1:
#             result_string += i
#         elif i == " " and flag_1 and not flag_2:
#             flag_2 = True
#             result_string += i
#         elif i != " ":
#             flag_1 = True
#             flag_2 = False
#             result_string += i
#
#     return result_string.rstrip()
# Please try pay attention to flags. They help us manipulate the logic.
# If you have some questions about implementation - let me know.
