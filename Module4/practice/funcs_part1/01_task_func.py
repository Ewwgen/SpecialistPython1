# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(n1, n2, n3, n4):
    # TODO: your code here
    pass

def max4(n1, n2, n3, n4):
    list_num = [n1, n2, n3, n4]
    list_num.sort(reverse=True)
    print(list_num[0])
    pass

max4(1,2,3,4)
# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
