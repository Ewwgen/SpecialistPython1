# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# import random
numbers = []
n = int(input('Введите целое число: '))
i = 0
while i < n:
  numbers.append(random.randint(-10, 10))
  i +=1

print('Список состоит из чисел: ', *numbers)
summa = 0
for i in numbers:
  if i >=0:
    summa += i
print('Сумма всех положительных чисел списка равна ', summa)
