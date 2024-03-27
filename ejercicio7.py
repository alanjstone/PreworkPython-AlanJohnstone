'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''
def simple_calculator():
  number_1 = int(input("Ingrese un numero: "))
  number_2 = int(input("Ingrese otro numero: "))
  operation = input("Indique que operacion quiere realizar(Suma, Resta, Multiplicacion, Division) con esos numeros: ")
  
  if operation.lower() == "suma":
    total = number_1 + number_2
    print(f"{number_1} mas {number_2} es {total}")
  elif operation.lower() == "resta":
    total = number_1 - number_2
    print(f"{number_1} restado por {number_2} es {total}")
  elif operation.lower() == "division":
    if number_2 == 0:
      print("No se puede dividir por 0")
    total = number_1 / number_2
    print(f"{number_1} dividido por {number_2} es {total}")
  elif operation.lower() == "multiplicacion":
    total = number_1 * number_2
    print(f"{number_1} multiplicado por {number_2} es {total}")
  else:
    print("No se reconoce la operacion ingresada")

simple_calculator()