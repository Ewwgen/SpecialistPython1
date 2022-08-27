# Создайте словарь из строки следующим образом:
# в качестве ключей возьмите буквы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.

# Пример: для строки 'pythonist'
# Получим словарь: {'p': 1, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 's': 1, 'i': 1}
# Примечание: т.к. ключи неупорядочены, порядок следования ключей может быть произвольным
~~~python 
string = input("Введите произвольную строку:")
dict_keys =[]

for letter in string.replace(" ", ""):
    dict_keys.append(letter)
dict_keys_unique = set(dict_keys)

dict_letters_count = dict.fromkeys(dict_keys_unique)

for letter in string.replace(" ", ""):
    if dict_letters_count[letter] is None:
        dict_letters_count[letter] = 0
        dict_letters_count[letter] += 1
    else:
        dict_letters_count[letter] += 1

print(dict_letters_count)
