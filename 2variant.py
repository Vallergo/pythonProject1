import math

from math import tan, pi, ceil
import time

z = int(input("Ведите номер задачи: "))

if(z == 1):
 def Zadach1(s, n):
    return (n * s ** 2) / (4 * tan(pi / n))
 s = float(input("Введите длинну стороны: "))
 n = ceil(float(input("Введите кол-во сторон: ")))
 print("Площадь равна: ", Zadach1(s, n))

elif(z==2):
 def Zadach2(ch):
    return (ceil((ch * (ch + 1)) / 2))
 ch = int(input("Введите положительное число: "))
 print("Сумма первых ", ch, " чисел равна: ", Zadach2(ch))
 
elif(z==3):
 def Zadach3():
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
