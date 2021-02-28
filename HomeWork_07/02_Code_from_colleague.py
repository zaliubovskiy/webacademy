import random

def pass_generator():
    lower_letters = lambda: chr(random.randint(97, 122))
    upper_letters = lambda: chr(random.randint(65, 90))
    numbers = lambda: chr(random.randint(48, 57))
    underscore = lambda: chr(95)
    list_of_values = [numbers, lower_letters, upper_letters, underscore]
    must_rules = {
        "underscore": (underscore, 1),
        "upper_letters": (upper_letters, 2)
    }
    choose_flow = [0, 1]
    password = []
    for rule in must_rules.values():
        password.extend([rule[0]() for _ in range(rule[1])])
    nums_counter = 0
    elements_existed_in_pass = sum([rule[1] for rule in must_rules.values()])
    for index, value_from_range in enumerate(range(random.randint(6, 20) - elements_existed_in_pass),
                                             start=elements_existed_in_pass):
        if password[index - 1].isdigit() or nums_counter == 5:
            symbol = list_of_values[1]
        else:
            symbol = list_of_values[random.choice(choose_flow)]
            if symbol().isdigit():
                nums_counter += 1
        password.append(symbol())
    random.shuffle(password)
    for i, v in enumerate(password):
        if v.isdigit() and password[i - 1].isdigit():
            password[i] = chr(random.randint(97, 122))
    return "".join(password)


def test_password(password):
    uppers = 0
    underscore = 0
    for i, v in enumerate(password):
        if i != 0 and v.isdigit():
            assert not password[i - 1].isdigit()
        if v.isupper():
            uppers += 1
        elif v == "_":
            underscore += 1
    assert underscore == 1, "Underscore more or less than 1"
    assert uppers >= 2, "Less than 2 Upper letters"


if __name__ == "__main__":
    for i in range(13):
        password = pass_generator()
        print(password)
        test_password(password)