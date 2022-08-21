# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один

for key, value in dictionary_2.items():
    dictionary_1[key]=value

print(dictionary_1)

----------
dictionary_1.update(dictionary_2)
