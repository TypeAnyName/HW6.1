errors = {'out': 'Вы вышли из системы ',
          'noaccess': 'У вас нет доступа в этот раздел',
          'unknown': 'Неизвестная ошибка',
          'timeout': 'Система долго не отвечает',
          'robot': 'Ваши действия похожи на робота'}


def get_errors(*args):
    answer = []
    for i in args:
      errors_list = errors.get(i)
      answer.append(errors_list)
    return answer


