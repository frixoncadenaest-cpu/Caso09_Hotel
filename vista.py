class VistaHotel:
    def mostrar_menu(self):
        print("\n--- HOTEL MIRADOR ---")
        print("1. Registrar tipo de habitación")
        print("2. Mostrar tipos de habitación")
        print("3. Reservar habitaciones")
        print("4. Salir")

    def pedir_opcion(self):
        return input("Seleccione una opción: ").strip()

    def pedir_datos_registro(self):
        tipo = input("Ingrese el tipo de habitación: ")
        precio = input("Ingrese el precio por noche: ")
        disponibles = input("Ingrese la cantidad disponible: ")
        return tipo, precio, disponibles

    def pedir_datos_reserva(self):
        codigo = input("Ingrese el código de habitación: ")
        cantidad = input("Ingrese la cantidad a reservar: ")
        return codigo, cantidad

    def mostrar_habitaciones(self, habitaciones):
        print("\nCódigo   | Tipo            | Precio/noche | Disponibles")
        print("-" * 54)
        for habitacion in habitaciones:
            print(habitacion)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)