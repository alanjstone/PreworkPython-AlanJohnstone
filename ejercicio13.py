'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''
def prime_verifier(number):
  if number == 1:
    print("1 no es primo")
  divisible_by = [] # numeros que lo dividen entero
  for n in range(2,number+1): # numeros entre 2 y el numero
    if number%n == 0: # mira el resto de la division
      divisible_by.append(n)
  if len(divisible_by) > 1:
    print(f"{number} no es primo")
  else:
    print(f"{number} es primo")

prime_verifier(100)