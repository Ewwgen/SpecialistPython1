## "Трехзначное ли"

### Задание

Проверьте, является ли данное число трехзначным.

### Формат входных данных

Дано целое число.

### Формат выходных данных

Вывести "Да", если данное число трехзначное и "Нет" в противоположном случае.

### Решение задачи

```python
a = int(input())

if  100 <= a <= 999:
    print('3 digit')
else:
    print('no 3 digit')
```

---
