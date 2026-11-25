class ControladorTienda:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion=self.vista.mostrar_menu()
            if opcion == "1":
                try:
                    nombre, precio, stock = self.vista.pedir_datos_registro()
                    precio = float(precio)
                    stock = int(stock)
                    registrado, mensaje = self.modelo.registrar(nombre, precio, stock)
                    if registrado:
                        self.vista.mensaje(mensaje)
                    else:
                        self.vista.error(mensaje)
                except ValueError:
                    self.vista.error("Datos ingresados incorrectamente")
            elif opcion == "2":
                self.vista.mostrar_productos(self.modelo.listar())
            elif opcion == "3":
                try:
                    codigo, cantidad = self.vista.pedir_datos_venta()
                    codigo = int(codigo)
                    cantidad = int(cantidad)
                    vendido, mensaje = self.modelo.operar_venta(codigo, cantidad)
                    if vendido:
                        self.vista.mensaje(mensaje)
                    else:
                        self.vista.error(mensaje)
                except ValueError:
                    self.vista.error("Datos ingresados incorrectamente")
            elif opcion == "4":
                print("Gracias por usar el programa")
                break
            else:
                print("Opcion no válida")