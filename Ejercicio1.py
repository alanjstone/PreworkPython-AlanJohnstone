'''
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''
# formula = (0°C × 9/5) + 32 = 32°F (segun Google)

def temp_converter(temp):
    temp_f = (temp * 9/5) + 32
    return temp_f

print(temp_converter(28.5))