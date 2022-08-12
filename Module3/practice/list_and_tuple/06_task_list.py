# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Первое число: " ))     # Первое число
second_number = int(input("Второе число: " ))    # Второе число

number = 0

while number <= second_number -1:
  number += 1
  if number % 3 == 0:
    print(number)
# TODO: your code here
