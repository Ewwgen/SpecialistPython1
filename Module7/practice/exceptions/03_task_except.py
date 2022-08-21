# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.
stroka= input('Введите 5 целых чисел через пробел')
chisla =[]
chisla_sorted =[]
try:
    for i in stroka.split():
        chisla.append(int(i))
    chisla_sorted.append(sorted(chisla))
    #print(*chisla_sorted)

    celye_chisla =[]
    #print(chisla_sorted[0])
    for i in chisla_sorted[0]:
       if  int(i) >= 0:
           celye_chisla.append(i)

    print(sorted(celye_chisla)[0])
except BaseException:
    print('Ошибка')
