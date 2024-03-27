'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''
def even_odds():
  user_list = list(input("ingrese una lista de valores separados por coma: "))
  evens = []
  odds = []
  # mas eficiente hacer a = user_list.split(",") y trabajar con a
  for n in user_list:
    if n == ",":
      i = user_list.index(n)
      user_list.pop(i)
  for n in user_list:
    if int(n)%2 == 0: # ver que los numeros sean pares o no
      evens.append(n)
    else:
      odds.append(n)
  print(f"su lista es: {user_list}")
  if len(evens) > 0:
    print("en ella hay " + f"{len(evens)}" + f" pares y son estos: {evens}")
  elif len(odds) > 0:
    print("en ella hay " + f"{len(odds)}" + f" impares y son estos: {odds}")

even_odds()