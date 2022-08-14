# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# TODO: your code here
некорректно

def drob(chelaya, chislitel, znamenatel):
    chislitel = chislitel + chelaya * znamenatel
    return chislitel, znamenatel

def plus(chislitel, znamenatel,chislitel2, znamenatel2):
    return  chislitel * znamenatel2 + chislitel2 * znamenatel, \
            znamenatel*znamenatel2

def minus(chislitel, znamenatel,chislitel2, znamenatel2):
    return  chislitel * znamenatel2 - chislitel2 * znamenatel, \
            znamenatel*znamenatel2


stroka ='5/6 + 4/7'
list = stroka.split(' ')
chislitel1 = None
znamenatel1 = None
chislitel2 = None
znamenatel2 = None

for i in range(len(list)-1):
    if not '/' in list[i] and not '+' in list[i] and not '-' in list[i]:
        if '/' in list[i+1]:
            temp_str =list[i+1].split('/')
            chislitel1, znamenatel1 = drob(int(list[i]), int(temp_str[0]),int(temp_str[1]))
        else:
            chislitel1 = list[i]
            znamenatel1 = 1
            list[i] = f'{chislitel1}/{znamenatel1}'
print(list)

