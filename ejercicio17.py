'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros
'''
def miles_to_km():
  user_miles = int(input("Ingrese las millas en numero: "))
  one_km = 1.60934
  km = user_miles * one_km
  print(f"{user_miles} millas son {km} kilometros")

miles_to_km()