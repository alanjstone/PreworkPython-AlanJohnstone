'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''
def tip_calculator(amount):
    tip = amount * 0.15
    total_tip = amount + tip
    
    print(f"La propina es {tip}, el total mas propina es {total_tip}")

tip_calculator(15)