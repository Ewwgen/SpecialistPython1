# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
import random
numbers = []
n = int(input('Введите целое число: '))
i = 0
while i < n:
  numbers.append(random.randint(0, 100))
  i +=1
print('Список состоит из чисел:' , *numbers)

numbers_upd = []
for i in numbers:
  if round(i ** (1/2),0)-(i ** (1/2)) == 0:
    numbers_upd.append(i ** (1/2))

print('Новый список состоит из чисел:',  numbers_upd)
