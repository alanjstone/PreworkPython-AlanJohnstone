'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''
def vowel_counter():
  print("Contamos vocales")
  palabra = input("Escriba una palabra o frase: ")
  vowels = ['a', 'e', 'i', 'o', 'u']
  vowel_quantity = 0
  for letter in palabra:
    if letter in vowels:
      vowel_quantity += 1
  
  print(vowel_quantity)

vowel_counter()
