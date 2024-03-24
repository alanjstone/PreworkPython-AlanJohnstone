'''
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''
def currency_converter():
  dolars = input("Cantidad de dolares a convertir: ")
  euros = int(dolars) * 0.85
  print(f"{dolars} dolares son {euros} euros")

currency_converter()