# 3seq.py
first_list = input("Введите элементы 1-го списка (через запятую): ").split(',')
second_list = input("Введите элементы 2-го списка (через запятую): ").split(',')

result_list = [x for x in first_list if x not in second_list]
print("Результат:", result_list)