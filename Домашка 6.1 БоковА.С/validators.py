def check_pin(pin):
    result = ""
    if len(pin) != 4:
        result = False
    else:
        for b in pin:
            if pin.count(b) == 4:
                result = False
            else:
                if pin == "1234":
                    result = False
                else:
                    result = True

    return (f"Пин: {result}")


def check_pass(password):
    check_num = ""
    check_letters = ""
    result = ""
    for i in password:
        if len(password) < 8:
            result = False
        else:
            if i.isdigit():
                check_num = True
            elif i.isalpha():
                check_letters = True
            else:
                result = False
    if check_num and check_letters == True:
        result = True
    else:
        result = False
    return (f"Пароль: {result}")


def check_mail(mail):
    result = ""
    if "@" in mail:
        if "." in mail:
            result = True
        else:
            result = False
    else:
        result = False

    return (f"Почта: {result}")


alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '


def check_name(name):
    result = ""
    name = name.upper()
    for i in name:
        if i not in alphabet:
            result = False
            break
        else:
            result = True
    return (f"Имя: {result}")
