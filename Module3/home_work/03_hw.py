# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
numbers = []
n = int(input('Введите целое число: '))
i = 0
while i < n:
  numbers.append(random.randint(-100, 100))
  i +=1
print('Список состоит из чисел:' , *numbers)

summa = 0
for j in numbers:
  if j >= 0 and j % 2 == 0:
    summa += j
print('Сумма всех положительных элементов кратных двум: ', summa)
