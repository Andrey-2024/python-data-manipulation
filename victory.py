# victory.py
import random

people = {
    'Иван Иванов': '02.01.1988',
    'Петр Петров': '15.02.1990',
    'Сергей Сергеев': '23.03.1985',
    'Анна Аннова': '10.04.1992',
    'Мария Маркова': '05.05.1980',
    'Николай Николаев': '12.06.1988',
    'Ольга Ольгова': '21.07.1990',
    'Дмитрий Дмитриев': '30.08.1985',
    'Елена Еленова': '19.09.1991',
    'Алексей Алексеев': '28.10.1989'
}

selected_people = random.sample(list(people.items()), 5)
correct_answers = 0

for person, birthday in selected_people:
    answer = input(f"Введите дату рождения {person} (в формате 'dd.mm.yyyy'): ")
    if answer == birthday:
        correct_answers += 1
    else:
        print(f"Неверно, правильная дата: {birthday}")

print(f"Количество правильных ответов: {correct_answers}")
print(f"Количество неправильных ответов: {5 - correct_answers}")