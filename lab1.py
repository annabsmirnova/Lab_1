import json
import re

f = open('pokemon_full.json')
file = f.read()
print('Общее количество символов в файле - ', len(file))

file_without_punctuation = re.sub(r'[^-\w]','', file) #Я считала, что дефис это не знак препинания, в файле (-) используется как дефис
print('Количесвто символов в файле без учета пробелов и знаков препинания - ', len(file_without_punctuation))

f.seek(0)
file = json.load(f)
f.close()
m = 0
n = len(file)
for i in range(0, n):
    if m < len(file[i]['description']):
        m = len(file[i]['description'])
        max_name = file[i]['name']
print('Имя покемона с самым длинным описанием - ', max_name)

max_slov = 0
all_max_ability = []
for i in range(0, n):
    abilities = file[i]['abilities']
    for one_ability in abilities:
        if max_slov < len(one_ability.split()):
            max_ability = one_ability
            max_slov = len(one_ability.split())
            all_max_ability = [one_ability]
        elif max_slov == len(one_ability.split()):
            all_max_ability.append(one_ability)
print('Умение, которое содержит больше всего слов - ', *all_max_ability)

