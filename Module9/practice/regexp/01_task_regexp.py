# Дано произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
# Найдите:
# 1) первое слово из строки
# 2) первые два символа каждого слова
# 3) все слова начинающиеся на гласную букву
# 4) все слова начинающиеся на согласную букву
# 5) все уникальные(без дубликатов) знаки препинания

text = 'Дано произвольное предложение. Слова разделены? пробелами. Это предложение, содержит знаки препинания.'

result1 = re.search(r'\w+\s', text)
#print(result1)

result2 = re.findall(r'(\w{2})\w+', text)
#print(result2)

result3 = re.findall(r'\b[АОИЕЁЭЫУЮЯ]\w+', text)
#print(result3)

result4 = re.findall(r'\b[^АОИЕЁЭЫУЮЯ]\w+', text)
#print(result4)

result5 = re.findall(r'\W(?!\S)', text)
print(set(result5))
