'''
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def palindromos():
  word = input("escriba una palabra: ")
  reverse_word = word[::-1]
  if word == reverse_word:
    print("es un palindromo")
  else:
    print("no es palindromo")

palindromos()