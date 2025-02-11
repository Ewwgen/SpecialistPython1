## "Улучшенный кассовый аппарат"

### Задание
Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров. \
Файл [data/items_sold.txt](data/items_sold.txt) - продажи всех товаров за день. \
Каждая строка файла - покупка одного покупателя.

Узнайте:
1. Какова общая выручка магазина
2. Какова выручка магазина по каждому типу товаров
3. Какой тип товара был продан на самую большую сумму
4. Сколько различных типов товаров было продано за день

### Формат входных данных

Дан текстовый файл. На каждой строке записана информация о проданных товарах в формате:

**тип_товара:цена**, например **fruits:45.10**

Все проданные товары разделены одним или более пробелами.

### Формат выходных данных

Вывести:
1. Какова общая выручка магазина
2. Какова выручка магазина по каждому типу товаров
3. Какой тип товара был продан на самую большую сумму. Если таких несколько, вывести любой.
4. Сколько различных типов товаров было продано за день

### Решение задачи

```python
stroka = []
numbers = {}
with open('items_sold', "r", encoding='UTF-8') as f:
    for line in f:
        stroka = line.split()
        for i in stroka:
            #numbers[]
            numbers[i.split(':')[0]] = float(i.split(':')[1])
print('Выручка магазина по каждому типу товаров: ')
for key in numbers.keys():
    print(key,':',numbers[key])

a = 0
for value in numbers.values():
    if value > a:
        a = value

sorted_numbers = sorted(numbers.items(), key=lambda item: item[1])
#print(sorted_numbers[-1])

print(f'Общая выручка магазина: {sum(numbers.values())}\n'
      f'{len(numbers)} различных типов товаров было продано за день\n'
      f'Тип товара был продан на самую большую сумму: {sorted_numbers[-1][0]}')
```

---
