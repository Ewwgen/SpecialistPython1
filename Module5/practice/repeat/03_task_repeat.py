# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

from Functions.palindrom import isPalindrom

a = 1
b = 99999
for i in range (a,b+1):
    if isPalindrom(i):
        print(i)
