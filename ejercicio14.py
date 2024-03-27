'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''
def discount_calc(price):
  discout = price * 0.2
  print(f"El descuento es de: {discout}")
  new_price = price - discout
  print(f"El precio final es: {new_price}")

discount_calc(100)