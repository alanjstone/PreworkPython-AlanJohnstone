'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''
def is_bisiesto():
  user_input = input("Escriba un año en numeros: ")
  if int(user_input)%4 == 0:
    print(f"El año {user_input} es bisiesto")
  else:
    print(f"El año {user_input} no es bisiesto")
    
is_bisiesto()