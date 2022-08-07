## "Дружественные числа"

### Задание

Два натуральных числа называются дружественными, если каждое из них равно сумме всех натуральных делителей другого
(само число при этом не рассматривается в качестве собственного делителя). \
Необходимо найти все пары натуральных дружественных чисел (не равных друг другу), до введенного числа.

### Формат входных данных

Дано одно целое положительное число

### Формат выходных данных

Вывести все пары дружественных чисел, удовлетворяющие условию задачи.

### Решение задачи

```python
a = int(input("a: "))
backup_a=a
delimiter = 2
summa = 0

while a != 1:
    if delimiter == backup_a:
        summa = 1
        break
    elif a % delimiter == 0:
        a //= delimiter
        print(a, delimiter)
        summa += delimiter
    else:
        delimiter += 1

b = int(input("b: "))
delimiter = 2
summa2 = 0
backup_b=b

while b != 1:
    if delimiter == backup_b:
        summa = 1
        break
    elif b % delimiter == 0:
        b //= delimiter
        print(b, delimiter)
        summa += delimiter
    else:
        delimiter += 1

if summa == summa2:
    print (a, b)
```

---

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|  300  | 220 284 |
