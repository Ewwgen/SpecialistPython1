# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here
tup = (2, 4, 6, -4, 12, 0, 5)
tup_list =[]
for i in tup:
    tup_list.append(i)

tup_list.sort()

print(tup_list[-1])
