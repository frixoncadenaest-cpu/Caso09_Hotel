class TipoHabitacion:
    def __init__(self, codigo, tipo, precio, disponibles):
        self.codigo = codigo
        self.tipo = tipo
        self.precio = precio
        self.disponibles = disponibles

    def validar(self):
        if self.codigo <= 0:
            return False, "El código debe ser mayor que cero."
        if not self.tipo or not self.tipo.strip():
            return False, "El tipo de habitación no puede estar vacío."
        if self.precio <= 0:
            return False, "El precio debe ser mayor que cero."
        if self.disponibles < 0:
            return False, "Las habitaciones disponibles no pueden ser negativas."
        return True, ""

    def reservar(self, cantidad):
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que cero."
        if cantidad > self.disponibles:
            return False, f"Error: solo hay {self.disponibles} habitaciones."
        self.disponibles -= cantidad
        return True, f"Listo. Quedan {self.disponibles} habitaciones."

    def __str__(self):
        return (
            f"{self.codigo:<8} | {self.tipo:<15} | "
            f"{self.precio:>10.2f} | {self.disponibles:>11}"
        )


class GestorHabitaciones:
    def __init__(self):
        self.habitaciones = [
            TipoHabitacion(1, "Simple", 35.00, 10),
            TipoHabitacion(2, "Doble", 55.00, 8),
        ]

    def listar(self):
        return self.habitaciones

    def buscar(self, codigo):
        for habitacion in self.habitaciones:
            if habitacion.codigo == codigo:
                return habitacion
        return None

    def registrar(self, tipo, precio, disponibles):
        nuevo_codigo = len(self.habitaciones) + 1
        nueva = TipoHabitacion(nuevo_codigo, tipo.strip(), precio, disponibles)
        valido, mensaje = nueva.validar()
        if not valido:
            return False, mensaje
        self.habitaciones.append(nueva)
        return True, f"Registrado con el código {nuevo_codigo}."

    def operar_reserva(self, codigo, cantidad):
        habitacion = self.buscar(codigo)
        if habitacion is None:
            return False, "Error: no existe ese código."
        return habitacion.reservar(cantidad)