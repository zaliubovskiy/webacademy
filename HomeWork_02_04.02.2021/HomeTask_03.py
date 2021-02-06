# Task 3 =================================================================================

# ТЗ: Создать программу, которая будет подсчитывать, достаточен ли доход пользователя,
# что бы прожить определенный срок в определенной стране.

# Developer notes: Тут специально дано неполное и невнятное ТЗ.
# Ваша задача, перед тем как приступить к решению, задать все необходимые вопросы
# "заказчику". А после, основываясь на ответах, приступить к решению.
# ========================================================================================
# Дано 3 страны. В каждой из них есть по 3 главных параментра:
# 1. Оренда жилья
# 2. Пропитание
# 3. Налоги
# Ваша задача: Самостоятельно выбрать 3 любые страны, задать им по 3 параметра, указанные выше.
# Запросить у пользователья его месячный доход.
# Посчитать, в какой стране он сможет прожить, что бы не уйти в минус по деньгам.

# Ukraine
rent_ua = 220
food_ua = 160
taxes_ua = 200
expenses_ua = rent_ua + food_ua + taxes_ua

# Norway
rent_no = 1400
food_no = 1200
taxes_no = 1150
expenses_no = rent_no + food_no + taxes_no

# Canada
rent_ca = 1100
food_ca = 600
taxes_ca = 500
expenses_ca = rent_ca + food_ca + taxes_ca

monthly_income = int(input("Please enter your average monthly income: "))

if monthly_income >= expenses_no:
    print("Congratulations, your income lets you decide among 3 countries: Norway, Canada, Ukraine")
elif monthly_income >= expenses_ca:
    print("With this income, you can decide whether to live in Canada or Ukraine")
elif monthly_income >= expenses_ua:
    print("You are doomed to live in Ukraine")
else:
    print("You gotta work harder, my friend!")
