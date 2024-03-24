'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no
'''
def age_verifyer():
  age_limit = 18
  user_age = input("Ingrese su edad en numeros: ")
  if int(user_age) < age_limit:
    print("Es menor de edad")
  else:
    print("Es mayor de edad")

age_verifyer()