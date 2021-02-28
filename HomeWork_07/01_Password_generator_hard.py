# завершить эту задачу согласно ТЗ и задекорировать функцию pass_generator так,
# что бы была возможность отследить колличество вызовов этой функции
# и сколько раз какой длинны был сгенерирован пароль
# (используйте замыкание во wrapper декоратора и словарь).

# ТЗ: Сгенерировать пароль для пользователя.
# Требования: длина от 6 до 20 символов, должен быть ровно один символ подчеркивания,
# хотя бы две заглавных буквы, не более 5 цифр, любые две цифры подряд недопустимы.

import random

# Generating a dictionary with all values = 0
pass_collector = {}
for i in range(6, 21):
    pass_collector.update({i: 0})
# Why this way didn't work for me: pass_collector.update({i: 0 for i in range(6, 21)}) ?


# Create a decorator that will count how may times your function is called
def func_counter(function):
    def wrapper():
        wrapper.count += 1
        res = function()
        print(f"Your function has been called {wrapper.count} times")
        return res
    wrapper.count = 0
    return wrapper


# Create a decorator which will track passwords and their lengths
# with the logic (key=Length of the password) : (value=How many times the password of this length is generated)
def pass_counter(function):
    def wrapper():
        res = function()
        pass_len = len(res)
        temp_var = pass_collector[pass_len]
        temp_var += 1
        pass_collector.update({pass_len: temp_var})
        return res
    return wrapper


@pass_counter
@func_counter
def password_generator():
    # PyCharm doesn't like Lambda expressions?
    letters = lambda: chr(random.randint(65, 90))
    password = "_"
    pass_length = random.randint(6, 20)

    # Adds a symbol of UPPERCASE letters until its done
    while len(password) < pass_length:
        symbol = letters()
        password += symbol

    # Convert the str to list in order to use "shuffle" method.
    list_pass = list(password)
    random.shuffle(list_pass)
    result_pass = "".join(list_pass)

    return result_pass
# Comment to my solution:
# There was nothing about the necessity of numbers, 0 <= 5 -> True
# There was nothing about the necessity of lowercase letters
# There was nothing about the maximum amount of uppercase letters, range(6, 20) >= 2 -> True
# I know that my simplifications make the password more vulnerable, but on the other hand,
# all conditions are met and the code consumes less memory and it took 10 strings to make it:)
# import this -> Simple is better than complex.


if __name__ == "__main__":
    for i in range(17):
        password_my = password_generator()
        print(password_my)
    print(pass_collector)
