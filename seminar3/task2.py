# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите количество элементов в массиве: "))
my_array = []
for i in range(n):
    my_array.append(int(input("Введите следующий элемент массива: ")))
x = int(input("Введите число для поиска: "))
min_delta = my_array[0] - x
flag = 1
for i in my_array:
    delta = i - x
    if not delta:
        print(f"Самое близкое число: {i}")
        flag = 0
        break
    else:
        if abs(delta) < min_delta:
            find_number = i
            min_delta = abs(delta)
if flag:
    print(f"Самое близкое число: {find_number}")
    

