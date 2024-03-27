'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''
week = {
  "1":"Lunes",
  "2":"Martes",
  "3":"Miercoles",
  "4":"Jueves",
  "5":"Viernes",
  "6":"Sabado",
  "7":"Domingo",
}
def week_day():
  user_input = input("Ingrese un numero del 1 al 7 para conocer el dia de la semana: ")
  if user_input in week:
    print(f"El {user_input} es {week[user_input]}")
  else:
    print(f"El {user_input} no corresponde con un dia de la semana.")

week_day()