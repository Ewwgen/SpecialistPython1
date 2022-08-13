# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
def circles (x1,y1,r1,x2,y2,r2):
 # ищем расстояние между двумя точками как гипотенузу треугольника
    abx = 0
    if x1 > x2:
        abx = x1 - x2
    else:
        abx = x2 - x1
    #print(abx)

    aby = 0
    if y1 > y2:
        aby = y1 - y2
    else:
        aby = y2 - y1
    #print(aby)
    ab = (abx**2+aby**2)**(1/2)

    if ab + r1 <= r2:
        print('Входит в окружность')
    else:
        print('Не входит в окружность')

circles(6,4,2,5,4,3)
