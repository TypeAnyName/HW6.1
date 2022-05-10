alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def shift_encode(string):
    string = string.upper()
    new_word = ''
    for i in string:
        position = alphabet.find(i)
        new_position = position + 1
        if i in alphabet:
            new_word += alphabet[new_position]
        else:
            new_word += i
    return new_word


def shift_decode(string):
    string = string.upper()
    new_word = ''
    for i in string:
        position = alphabet.find(i)
        new_position = position - 1
        if i in alphabet:
            new_word += alphabet[new_position]
        else:
            new_word += i
    return new_word
