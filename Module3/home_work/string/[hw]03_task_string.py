# Посчитайте количество согласных букв в данной строке.

text = ...

ВАРИАНТ# 1 - подсчет неуникальный:
  char_list=['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
text = input(str('Введите фразу:')).upper()
cnt_char=0
for i in text: 
  for j in char_list:
    if i == j:
        cnt_char += 1
print(cnt_char) 


ВАРИАНТ# 2 - Уникальное кол-во согласных:
char_list=['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
text = input(str('Введите фразу:')).upper()
upd_char_list=[]
for i in text: 
  for j in char_list:
    if i == j:
        upd_char_list.append(i)
print(len(set(upd_char_list)))
