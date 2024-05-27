# 2seq.py
elements = input("Введите элементы списка через запятую, точку с запятой или слэш: ")
if ',' in elements:
    delimiter = ','
elif ';' in elements:
    delimiter = ';'
else:
    delimiter = '/'

lst = elements.split(delimiter)
lst = [int(x) for x in lst]
unique_elements = [x for x in lst if lst.count(x) == 1]
print("Результат:", unique_elements)