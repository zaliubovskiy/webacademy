# Компьютер загадывает число от 1 до 100.
# У пользователя три попытки отгадать.
# После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число.

from random import randint

a = randint(1, 100)  # Randomly select a number in range from 1 to 100

while 1:  # Can I do it with the "for" cycle?
    b = int(input("Guess the number from 1 to 100: "))
    if a == b:
        print("Congratulations, you've guessed!")
        break
    elif a < b:
        print("Your number is greater than the computer guessed")
        b = int(input("Guess another number from 1 to 100: "))
        if a == b:
            print("Congratulations, you've guessed!")
            break
        elif a < b <= 100:
            print("Your number is greater than the computer guessed")
            b = int(input("Guess another number from 1 to 100: "))
            if a == b:
                print("Congratulations, you've guessed!")
                break
            else:
                print("Sorry, you didn't guess:( Try again next time!")
                break
        elif a > b <= 100:
            print("Your number is less than the computer guessed")
            b = int(input("Guess another number from 1 to 100: "))
            if a == b:
                print("Congratulations, you've guessed!")
                break
            else:
                print("Sorry, you didn't guess:( Try again next time!")
                break
    else:
        print("Your number is less than the computer guessed")
        b = int(input("Guess another number from 1 to 100: "))
        if a == b:
            print("Congratulations, you've guessed!")
            break
        elif a < b <= 100:
            print("Your number is greater than the computer guessed")
            b = int(input("Guess another number from 1 to 100: "))
            if a == b:
                print("Congratulations, you've guessed!")
                break
            else:
                print("Sorry, you didn't guess:( Try again next time!")
                break
        elif a > b <= 100:
            print("Your number is less than the computer guessed")
            b = int(input("Guess another number from 1 to 100: "))
            if a == b:
                print("Congratulations, you've guessed!")
                break
            else:
                print("Sorry, you didn't guess:( Try again next time!")
                break

# It is bad that there is no 'fool check'. We can enter all the numbers, not only from 1 to 100.
