# Пользователь вводит сумму вклада в банк и годовой процент.
# Найдите сумму вклада через 5 лет

deposit_amount = int(input("Please enter the amount of the deposit: "))
annual_interest = int(input("Please enter the annual interest: "))
years = 5

for i in range(years):
    result = deposit_amount / 100 * annual_interest  # counts income for every year
    deposit_amount += result

print(f"Your final amount would be: {deposit_amount}")
