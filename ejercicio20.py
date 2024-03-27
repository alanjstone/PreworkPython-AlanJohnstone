'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''
def sum_list():
  user_input = input("Ingrese una lista de valores separados por coma: ")
  total = 0
  user_list = user_input.split(",")
  for item in user_list:
    try:
      total += int(item)
    except TypeError:
      continue
    except ValueError:
      continue
  
  if total == 0:
    print("Su lista no contiene numeros.")
  else:
    print(f"El total de la suma de los numeros de la lista es: {total}")

sum_list()