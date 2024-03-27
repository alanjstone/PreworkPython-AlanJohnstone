'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''
# 1 hr = 60 min
def time_converter(time):
  hours = time//60
  minutes = time%60
  print(f"{time} minuto(s) son {hours} hora(s) y {minutes} minuto(s)")

time_converter(189)