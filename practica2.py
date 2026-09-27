"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches

class Coches:
    def __init__(self,color,marca,velocidad):
        self.__colorcolor = color
        self.__marcamarca= marca
        self.__velocidad= velocidad

    def acelerar (self):
        self.__velocidad+=1

    def frenar(self):
         self.__velocidad+=1

    def tocar_claxon(self):
        #print ("*pitazo*")
        return "*pitazo*"

#Instanciar o crear objetos de la clase Coches

coche1=Coches("Blanco","VW",220)
coche2=Coches("Azul","Nissan",180)

# print(f"El color del coche 1 es: {coche1.__color}")
# No se pueden usar los atributos porque son privados 

#Primera opcion
print(f"El claxon del coche 1 hace: {coche1.tocar_claxon()}")

#segunda opcion
print(f"El claxon del coche 1 hace:") 
coche2.tocar_claxon()

# Ejercicio de acelerar y frenar el coche 1
# print(f"El velocidad del coche 1 es:")
#coche1.acelerar()






