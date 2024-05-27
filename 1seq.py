# 1seq.py
n = int(input("Введите количество элементов: "))
lst = []
for i in range(n):
    elem = int(input(f"Введите {i+1} элемент: "))
    lst.append(elem)
lst.sort()
print("Вывод:", lst)