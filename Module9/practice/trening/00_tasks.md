## Практические задания на regExp

Ресурс для проверки регулярок: [тут](https://regex101.com/).

### Задание-0 “Разминка”

#### Часть-1:

Даны строки: **cats. 8967. ?=+!. abcd1**

Напишите шаблон, который будет соответствовать первым трем строкам, но не соответствовать последней.

Соответствовать: <font color="green">cats. </font>

Соответствовать: <font color="green">8967. </font>

Соответствовать: <font color="green">?=+!. </font>

Пропустить:		<font color="red">abcd1</font>

~~~~python
import re

test = 'cats. 8967. ?=+!. abcd1'

result1 = re.findall(r'[a-z0-9\W]{4}[.]', test)

print(result1)

#### Часть-2:
Даны строки: **can man fan dan**

Напишите шаблон, который будет соответствовать первым трем строкам, но не соответствовать трем последним.\

Соответствовать	<font color="green">can</font>

Соответствовать	<font color="green">man</font>

Соответствовать	<font color="green">fan</font>

Пропустить		<font color="red">dan</font>

Пропустить		<font color="red">ran</font>

Пропустить		<font color="red">pan</font>

~~~python
import re

test = 'can man ran fan pan'

result1 = re.findall(r'[cfm].{2}\s', test)

print(result1)


#### Часть-3:

Для строк ниже напишите выражение, которое будет соответствовать как полной дате, так и только годам.

Точно известно: название месяца начинается с большой буквы и состоит из трех букв. \
А год состоит из четырех цифр.

~~~python

import re

test = 'Date 1987'

result1 = re.findall(r'[A-Z]{1}[a-z]{2}\s\d{4}|\d{4}', test)

print(result1)


| Дано                          | Извлечь-1         | Извлечь-2 |
| -----------------             | -----------       |----------- |
| Date Jan 1987                 | Jan 1987          |1987
| In May 1969                   | May 1969          |1969
| The war ended on 8 May 1945   | May 1945          |1945

