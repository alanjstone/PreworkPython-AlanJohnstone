'''
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''
def word_counter():
  sentence = input("Escriba una oracion: ")
  words = sentence.split(" ")
  print(f"Su oracion tiene {len(words)} palabras:")
  print(words)
  
word_counter()