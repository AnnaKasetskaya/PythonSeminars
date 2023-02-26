# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две 
# подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random
number1 = random.randint(0, 1000)
number2 = random.randint(0,1000)
summa = number1 + number2
print(f"Сумма чисел: {summa}")
compos = number1 * number2
print(f"Произведение чисел: {compos}")
flag = 0
for i in range(1001):
    for j in range(1001):
        if ((i * j == compos) and (i + j == summa)):
            print(i, j)
            flag = 1
            break
    if flag: 
        break