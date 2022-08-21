# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random

lst = [random.randint(-10,10) for _ in range(random.randint(1,7))]

x1 = 0
x2 = 0
x3_ = 0
x3 = 0
for i in lst:
    if i<10:
        x1 +=1
    if i >= 0:
        x2 += i
    if i%2 ==0:
        x3_ +=1
        x3 += i
print(lst)
print(f'Количество элементов списка не превышающие 10: {x1} '
      f'\nСумма всех положительных элементов списка: {x2}'
      f'\nСреднее арифметическое всех четных элементов: {x3/x3_}')
