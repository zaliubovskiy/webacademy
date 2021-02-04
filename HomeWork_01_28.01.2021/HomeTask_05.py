# Пользователь вводит четыре числа. Найдите наибольшее четное число среди них.
# Если оно не существует, выведите фразу "not found"

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the first number: "))
num_3 = int(input("Enter the first number: "))
num_4 = int(input("Enter the first number: "))

if num_1 % 2 == 0:
    if num_2 % 2 == 0:
        if num_3 % 2 == 0:
            if num_4 % 2 == 0:  # ALl the numbers are even
                if num_1 > num_2 > num_3 > num_4:
                    print(num_1)
                else:
                    if num_2 > num_3 > num_4:
                        print(num_2)
                    else:
                        if num_3 > num_4:
                            print(num_3)
                        else:
                            print(num_4)
            else:  # num_1, num_2, num_3 are even, num_4 is odd
                if num_1 > num_2 > num_3:
                    print(num_1)
                else:
                    if num_2 > num_3:
                        print(num_2)
                    else:
                        print(num_3)
        else:
            if num_4 % 2 == 0:  # num_1, num_2, num_4 are even, num_3 is odd
                if num_1 > num_2 > num_4:
                    print(num_1)
                else:
                    if num_2 > num_4:
                        print(num_2)
                    else:
                        print(num_4)
            else:
                if num_1 > num_2:
                    print(num_1)
                else:
                    print(num_2)
    else:
        if num_3 % 2 == 0:  # num_1, num_3  are even, num_3, num_4 are odd
            if num_4 % 2 == 0:
                if num_1 > num_3 > num_4:
                    print(num_1)
                else:
                    if num_3 > num_4:
                        print(num_3)
                    else:
                        print(num_4)
            else:
                if num_1 > num_3:
                    print(num_1)
                else:
                    print(num_3)
        else:
            if num_4 % 2 == 0:
                if num_1 > num_4:
                    print(num_1)
                else:
                    print(num_4)
            else:
                print(num_1)
else:
    if num_2 % 2 == 0:
        if num_3 % 2 == 0:
            if num_4 % 2 == 0:
                if num_2 > num_3 > num_4:
                    print(num_2)
                else:
                    if num_3 > num_4:
                        print(num_3)
                    else:
                        print(num_4)
            else:
                if num_2 > num_3:
                    print(num_2)
                else:
                    print(num_3)
        else:
            if num_4 % 2 == 0:
                if num_2 > num_4:
                    print(num_2)
                else:
                    print(num_4)
            else:
                print(num_2)
    else:
        if num_3 % 2 == 0:
            if num_4 % 2 == 0:
                if num_3 > num_4:
                    print(num_3)
                else:
                    print(num_4)
            else:
                print(num_3)
        else:
            if num_4 % 2 == 0:
                print(num_4)
            else:
                print("not found")
