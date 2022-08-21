# Напишите функцию декоратор, которая округляет значение декорируемой функции до двух знаков после  запятой.
# Если округление невозможно, например там строка, или не требуется(целое число) то оставляем результат без изменений.
# Примечание: используйте встроенную функцию round()


def decor_round(func):
    def wrapper(x):
        try:
            result = func(x)
            result = round(result, 2)
            return result
        except:
            return x
    return wrapper

@decor_round
def print_float(x):
    return x/2

print(print_float('aaa'))
