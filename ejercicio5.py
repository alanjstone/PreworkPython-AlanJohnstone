'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
total = 0
for number in range(1,101):
  if number%2 == 0:
    total += number
  
print(total)