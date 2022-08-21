# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)
def decor(func):
    def wrapper():
        result = func()
        for i in range(len(result) + 2):
            print("*", end="")
        print()
        print("*", end="")
        print(result, end="")
        print("*")
        for i in range(len(result) + 2):
            print("*", end="")

    return wrapper


@decor
def privet():
    return "Privet"


privet()
