# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты
# высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет
# N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число 
# ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора
# черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один
# заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий
# модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
bush_count = random.randint(3, 7)
bush_berry_count_list = [random.randint(10, 20) for i in range(bush_count)]
print(bush_count)
print(bush_berry_count_list)
max_berry_count = 0
for i in range(1, bush_count-1):
    if max_berry_count < (bush_berry_count_list[i - 1] + bush_berry_count_list[i] + bush_berry_count_list[i + 1]):
        max_berry_count = (bush_berry_count_list[i - 1] + bush_berry_count_list[i] + bush_berry_count_list[i + 1])
    i +=3
if max_berry_count < (bush_berry_count_list[-2] + bush_berry_count_list[-1] + bush_berry_count_list[0]):
    max_berry_count = (bush_berry_count_list[-2] + bush_berry_count_list[-1] + bush_berry_count_list[0])
print(max_berry_count)