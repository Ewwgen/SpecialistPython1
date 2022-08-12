## "Подсчет длинных слов"

### Задание

Определить в предоставленном сообщении количество слов длиной больше, чем 5.

### Формат входных данных

Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.

### Формат выходных данных

Вывести количество найденных слов.

### Решение задачи

```python
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
index = 0
words = []
while index > -1:
  index = text.find(' ')
  words.append(text[:index ])
  text = text[index+1:]

words_count = 0
for i in words:
  if len(i) > 5:
    words_count +=1
print(words_count)
```

---

