# Дано значение температуры в градусах Цельсия. Вывести температуру в градусах Фаренгейта.
# Цельсий х 1,8 + 32 = Фаренгейт

degrees_c = int(input("Enter the temperature in 'C': "))
degrees_f = (degrees_c * 1.8) + 32  # conversion to Fahrenheit

print(f"Your temperature in F: {degrees_f}")
