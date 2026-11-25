class ControladorTienda:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        opcion=""
        while opcion !="4":
            opcion=self.vista.mostrar_menu()
            if opcion == "1":
                try:
                    nombre, precio, stock= self.vista.pedir_opcion()
                    mensaje= self.modelo.registrar(nombre, precio, stock)
                    self.vista.mensaje("Procesado correctamente")
                except ValueError:
                    self.vista.error("Datos ingresados incorrectamente")
            elif opcion == "2":
                try:
                    self.vista.mostrar_productos(self.modelo.listar())
                except ValueError:
                    self.vista.mostrar_mensaje("Lista vacía")
            elif opcion == "3":
                try:
                    codigo, cantidad= self.modelo.vender()
                    restar= self.modelo.operar_venta(cantidad)
                    if restar == True:                        
                        self.vista.mensaje("Procesado correctamente")
                    else:
                        self.vista.error("No se pudo completar la venta")
                except ValueError:
                    self.vista.mostrar_mensaje("Datos ingresados incorrectamente")
            else:
                print("Gracias por usar el programa")
                break