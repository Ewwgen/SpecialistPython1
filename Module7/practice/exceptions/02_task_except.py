# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.
month_id = input('Введите номер месяца: ')
year_id = input('Введите номер года (4 символа): ')

def is_leap_year (year):
    result =False
    if int(year) % 100 ==0:
        result = int(year) %400 ==0
    else:
        result = int(year)%4 ==0
    return result
try:
    if month_id == 2:
        if is_leap_year(year_id):
            print(29)
        else:
         print(28)
    else:
       if int(month_id) // 2 == 0:
           if month_id == 8 or month_id == 12:
               print(31)
           else:
            print(30)
       else:
           print(31)
except BaseException:
    print(f'У вас ошибка: {TypeError}')
