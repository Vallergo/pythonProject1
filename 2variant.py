import math

from math import tan, pi, ceil
import time




z = int(input("Ведите номер задачи: "))
if(z == 1):

 def square(s, n):
    return (n * s ** 2) / (4 * tan(pi / n))

 s = float(input("Введите длинну стороны: "))
 n = ceil(float(input("Введите кол-во сторон: ")))
 print("Площадь равна: ", square(s, n))

elif(z==2):

 def sum(total):
    return (ceil((total * (total + 1)) / 2))
 total = int(input("Введите положительное число: "))
 print("Сумма первых ", total, " чисел равна: ", sum(total))
elif(z==3):

 def prov():
    gl = ['a','e','i','o','u','A','E','I','O','U']
    y = ['y','Y']
    w = input("Введите букву: ")
    if w in gl:
        print("Буква "+w+" гласная")
    elif w in y:
        print("Буква "+w+" может быить и гласной и согласной")
    else:
         print("Буква " + w + " согласная")


 prov()