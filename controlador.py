class ControladorHotel:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                self._opcion_registrar()
            elif opcion == "2":
                self._opcion_mostrar()
            elif opcion == "3":
                self._opcion_reservar()
            elif opcion == "4":
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida")

    def _opcion_registrar(self):
        tipo, precio_texto, disp_texto = self.vista.pedir_datos_registro()
        try:
            precio = float(precio_texto)
            disponibles = int(disp_texto)
        except ValueError:
            self.vista.mostrar_mensaje("Error: ingrese valores numéricos válidos.")
            return

        ok, mensaje = self.modelo.registrar(tipo, precio, disponibles)
        self.vista.mostrar_mensaje(mensaje)

    def _opcion_mostrar(self):
        habitaciones = self.modelo.listar()
        self.vista.mostrar_habitaciones(habitaciones)

    def _opcion_reservar(self):
        codigo_texto, cantidad_texto = self.vista.pedir_datos_reserva()
        try:
            codigo = int(codigo_texto)
            cantidad = int(cantidad_texto)
        except ValueError:
            self.vista.mostrar_mensaje("Error: ingrese números enteros válidos.")
            return

        ok, mensaje = self.modelo.operar_reserva(codigo, cantidad)
        self.vista.mostrar_mensaje(mensaje)