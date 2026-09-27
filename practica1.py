"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

base = float(input("Ingresa la base del rectangulo: "))

altura = float(input("Ingresa la altura del rectangulo: "))

area = calcular_area_rectangulo(base, altura)

print("El area del rectangulo es:", area)



#Implementar el paradigma Orientado a Objetos (OO)

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = float(input("\nIngresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))

rectangulo = Rectangulo(base, altura)

print("El area del rectangulo es:", rectangulo.calcular_area())

class rectangulos:
    def area(self,base,altura):
        areaR=base*altura
        return areaR

rectangulo1=rectangulos() #crear o instanciar un objecto "rectangulo1" de la clase "rectangulos"
print(f"El area del rectangulo es: {rectangulo1 . area(5,6)}")