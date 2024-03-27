'''
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
'''
# como argumento
def rectangle_area(width, lenght):
  area = lenght * width
  return area

print(rectangle_area(10,34))

# como input de usuario
longitud = int(input("Longitud del rectangulo (como numero): "))
ancho = int(input("Ancho del rectangulo (como numero): "))
area = longitud * ancho
print(area)