import json
import re

file = open('pokemon_full.json')
anime_str = file.read()
print('Общее количество символов в файле - ', len(anime_str))

anime_str_without_punctuation = re.sub(r'[^-\w]','', anime_str)
#Я считала, что дефис это не знак препинания.
#В файле (-) используется как дефис
print('Количесвто символов в файле '
      'без учета пробелов и знаков препинания - ',
      len(anime_str_without_punctuation))

file.seek(0)
anime_str = json.load(file)
file.close()
max_name_len = 0
len_anime_str = len(anime_str)
max_words = 0
all_max_ability = []
for pokemon in range(len_anime_str):
    description_len = len(anime_str[pokemon]['description'])
    if max_name_len < description_len:
        max_name_len = description_len
        max_name = anime_str[pokemon]['name']
    abilities = anime_str[pokemon]['abilities']
    for one_ability in abilities:
        abilitiy_len = len(one_ability.split())
        if max_words < abilitiy_len:
            max_ability = one_ability
            max_words = abilitiy_len
            all_max_ability = [one_ability]
        elif max_words == abilitiy_len:
            all_max_ability.append(one_ability)
print('Имя покемона с самым длинным описанием - ', max_name)
print('Умение, которое содержит больше всего слов - ', *all_max_ability)
