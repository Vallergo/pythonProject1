import math

print("Ведите номер задачи:")
z = int(input())
if(z == 1):
 def SUchAcr():
  print("Выбрана задача 1")
  print("Ведите ширину вашего участка в квадратных метрах")
  a = int(input())
  print("Ведите высоту вашего участка в квадратных метрах")
  b = int(input())
  s=a*b
  s =(s * 0.00025)
  print("Площадь в акрах равна",s)
 SUchAcr()
elif(z == 2):
 def UskorSvobodPad():
  print("Выбрана задача 2")
  print("Введите высоту с которой будет сброшен объект в метрах")
  a = int(input())
  Vt = math.sqrt(0*0+2*9.8*a)
  print("Ответ:",Vt)
 UskorSvobodPad()





