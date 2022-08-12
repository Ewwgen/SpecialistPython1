# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
import random
numbers = []
n = int(input('Введите целое число: '))
i = 0
while i < n:
  numbers.append(random.randint(-10, 10))
  i +=1

print('Список состоит из чисел: ', *numbers)
summa = 0
for i in numbers:
  summa += i
print('Сумма всех чисел списка равна ', summa)
