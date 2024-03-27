'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
# IMC = peso (kg)/ [estatura (m)]2

# input de usuario
def calc_imc():
  height = input("Su altura en cm: ")
  weight = input("Su peso en kg: ")
  imc = int(weight)/(int(height)*0.01)**2
  return imc

print(calc_imc())

# como argumentos
def imc_clac(height, weight):
  imc = weight/height**2
  print(imc)

imc_clac(1.8, 80)