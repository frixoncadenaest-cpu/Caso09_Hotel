class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def validar(self):
        if self.codigo <= 0:
            return False, "El código debe ser mayor que cero."
        if not self.nombre or not self.nombre.strip():
            return False, "El nombre del producto no puede estar vacío."
        if self.precio <= 0:
            return False, "El precio debe ser mayor que cero."
        if self.stock < 0:
            return False, "El stock no puede ser negativo."
        return True, ""

    def vender(self, cantidad):
        if cantidad <= 0:
            return False, "Error: la cantidad debe ser mayor que cero."
        if cantidad > self.stock:
            return False, f"Error: solo hay {self.stock} unidades."
        self.stock -= cantidad
        return True, f"Listo. Quedan {self.stock} unidades."

    def __str__(self):
        return (
            f"{self.codigo:<8} | {self.nombre:<15} | "
            f"{self.precio:>10.2f} | {self.stock:>10}"
        )


class GestorProductos:
    def __init__(self):
        self.productos = [
            Producto(1, "Arroz", 1.25, 40),
            Producto(2, "Aceite", 3.10, 15),
        ]

    def listar(self):
        return self.productos

    def buscar(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar(self, nombre, precio, stock):
        nuevo_codigo = len(self.productos) + 1
        nuevo = Producto(nuevo_codigo, nombre.strip(), precio, stock)
        valido, mensaje = nuevo.validar()
        if not valido:
            return False, mensaje
        self.productos.append(nuevo)
        return True, f"Registrado con el código {nuevo_codigo}."

    def operar_venta(self, codigo, cantidad):
        producto = self.buscar(codigo)
        if producto is None:
            return False, "Error: no existe ese código."
        return producto.vender(cantidad)