import validators

users_dict = {'1': {'name': 'Данил', 'email': 'local@skypro', 'password': 'secretd00r', 'pin': '1239'},
              '2': {'name': 'Р_и_т_а', 'email': 'you(at)sky.pro', 'password': 'huskyeye5', 'pin': '3333'},
              '3': {'name': 'К0нстантин', 'email': 'me@sky.pro', 'password': 'secret', 'pin': '1234'},
              '4': {'name': 'А Ф', 'email': '@lizaveta', 'password': 'm3wm3wm3w', 'pin': '00011'},
              '5': {'name': 'Елена', 'email': 'alarm@gmail.com', 'password': 'fh43j_!', 'pin': '# 8765'},
              }

user_input = input("Введите номер пользователя от 1 до 5\n")
print(f"Пользователь № {user_input}: {users_dict[user_input]['name']}\n")
print(validators.check_pin(users_dict[user_input]['pin']))
print(validators.check_pass(users_dict[user_input]["password"]))
print(validators.check_mail(users_dict[user_input]["email"]))
print(validators.check_name(users_dict[user_input]['name']))
