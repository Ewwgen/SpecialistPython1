# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

# TODO: your code here

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here

print("На складе самый дорогой товар брэнда(ов): ")

brands=[]
for i in items:
    brands.append((i['brand']).title())

print("Товары на складе представлены брэндами: ", end=''), print(*set(brands) , sep = ', ')

brands_dict = {} # создаем пустой словарь

for i in brands:
    brands_dict[i] = brands.count(i)

for key, value in  brands_dict.items():
    if value == max(brands_dict.values()):
        print("На складе больше всего товаров брэнда(ов): ", end=''), print(key)

prices =[]
for i in items:
    prices.append(i['price'])

max_price = 0
for i in prices:
    if i == max(prices):
        max_price = i

for i in items:
    if i['price'] == max_price:
        print("На складе самый дорогой товар брэнда(ов): ", end=''), print((i['brand']).title())
