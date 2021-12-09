import datetime
import math
import time

print("Ведите номер задачи:")
z = int(input())
if(z == 1):
 def DecorZad1():
  print("Выбрана задача 1")
  print("Время выполнения:", datetime.datetime.today().strftime("%H:%M:%S"))
  def SUchAcr():
   print("Ведите ширину вашего участка в квадратных метрах")
   a = int(input())
   print("Ведите высоту вашего участка в квадратных метрах")
   b = int(input())
   s=a*b
   s =(s * 0.00025)
   print("Площадь в акрах равна",s)
  SUchAcr()
 DecorZad1()
elif(z == 2):
 def DecorZad2():
  print("Выбрана задача 2")
  print("Время выполнения:", datetime.datetime.today().strftime("%H:%M:%S"))
  def UskorSvobodPad():

   print("Введите высоту с которой будет сброшен объект в метрах")
   a = int(input())
   Vt = math.sqrt(0*0+2*9.8*a)
   print("Ответ:",Vt)
  UskorSvobodPad()


 DecorZad2()





