import errors
import graphics
import encode_decode
print("Вывод ошибок:")
print(errors.get_errors("out", "unknown", "noaccess"))
print('')
print("Вывод псевдографики:")
graphics.draw_carpet(9, 4)
print('')
print("Вывод зашифровооного слова и дешефрованного:")
print(encode_decode.shift_encode('Привет как дела?'))
print(encode_decode.shift_decode("РСЙГЁУ ЛБЛ ЕЁМБ?"))

