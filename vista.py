class VistaTienda:
    def mostrar_menu(self):
        print("\n--- TIENDA DON LUCHO ---")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Vender producto")
        print("4. Salir")
        return self.pedir_opcion()

    def pedir_opcion(self):
        return input("Seleccione una opción: ").strip()

    def pedir_datos_registro(self):
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio: ")
        stock = input("Ingrese el stock: ")
        return nombre, precio, stock

    def pedir_datos_venta(self):
        codigo = input("Ingrese el código del producto: ")
        cantidad = input("Ingrese la cantidad a vender: ")
        return codigo, cantidad

    def mensaje(self, mensaje):
        print(mensaje)

    def error(self, mensaje):
        print(mensaje)

    def mostrar_productos(self, productos):
        print("\nCódigo   | Nombre          | Precio     | Stock")
        print("-" * 52)
        for producto in productos:
            print(producto)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)