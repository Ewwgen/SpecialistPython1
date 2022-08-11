# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here


names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
name_leng = 0
name_leng_list = []

for i in names:
  name_leng = len(i)
  name_leng_list.append(name_leng )

j = 0
for i in name_leng_list:
  j += 1
  if i == max(name_leng_list):        
    print(names[j-1])
