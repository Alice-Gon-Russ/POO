from coches import cochesBD, coches

class App:
    def __init__(self):
        self.main()

    def clear(self):
        print("\033c")

    def pause(self):
        input("... ¡Oprima cualquier tecla para continuar! ...")

    def respuestaSql(self, respuesta):
        if respuesta:
            input("...¡Accion realizada con exito!...")
        else:
            input("...¡No se pudo realizar la accion!...")

    # def datosCoche(self, tipo):
    #     marca = input("Marca: ").upper().strip()
    #     color = input("Color: ").upper().strip()
    #     modelo = input("Modelo: ").upper().strip()
    #     velocidad = input("Velocidad: ").strip()
    #     potencia = input("Potencia: ").strip()
    #     asientos = input("Asientos: ").strip()
    #     return marca, color, modelo, velocidad, potencia, asientos

    def datosCoche(self, tipo):
        cochesitos = {}
        cochesitos['marca'] = input("Marca: ").upper().strip()
        cochesitos['color'] = input("Color: ").upper().strip()
        cochesitos['modelo'] = input("Modelo: ").upper().strip()
        cochesitos ['velocidad'] = input("Velocidad: ").strip()
        cochesitos ['potencia'] = input("Potencia: ").strip()
        cochesitos ['asientos'] = input("Asientos: ").strip()
        return cochesitos

    def menuAcciones(self, tipo):
        print(f"\n\t\t\t...::: Menú de {tipo} :::... \n")
        opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n \t\tSeleccionar Opcion: ").strip()
        return opcion

    def menuCoche(self):
        opcion = True
        while opcion:
            self.clear()
            opcion = self.menuAcciones("Coches")
            match opcion:
                case '1':
                    self.clear()
                    cochesitos = self.datosCoche("Coche")
                    coche1 = cochesBD.CochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                    respuesta = coche1.insertar()
                    self.respuestaSql(respuesta)
                    del coche1
                case '2':
                    self.clear()
                    id = input("ID del coche a eliminar: ").strip()
                    respuesta = cochesBD.CochesBD.eliminar(id)
                    self.respuestaSql(respuesta)
                case '3':
                    id = input("ID del coche a actualizar: ").strip()
                    cochesitos = self.datosCoche("Coche")
                    coche1 = cochesBD.CochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                    respuesta = coche1.actualizar(id)
                    self.respuestaSql(respuesta)
                    del coche1
                case '4':
                    self.clear()
                    registros = cochesBD.CochesBD.consultar()
                    if len(registros)>0:
                        numCoches = 1
                        for fila in registros:
                            print(f"Coche #{numCoches}\nID: {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\n Potencia: {fila[5]}\n Asientos: {fila[6]}")
                            numCoches += 1
                            self.pause()
                    else:
                        print("\n\n\t...¡Por el momento no hay datos que mostrar!...")
                    del coche1
                case _:
                    input("...¡Opción invalida!...")


    def main(self):
        opcion = True
        while opcion:
            self.clear()
            print("\n\t\t\t...::: M E N U  P R I N C I P A L :::... \n")
            opcion=input("\n\t 1.- Coches \n\t 2.- Salir \n\t \n\n\t\tSeleccionar Opcion: ").strip()

            match opcion:
                case "1":
                    self.clear()
                    self.menuCoche()
                    self.pause()

                case "2":
                    self.clear()
                    print("\n\t...Salir del sistema...")
                    opcion = False
                case _:
                    input("\n\t...¡Opción inválida!...")


if __name__ == "__main__":
    app = App()
