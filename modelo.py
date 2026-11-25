class TipoHabitacion:
    def __init__(self, codigo, tipo, precio, disponibles):
        self.codigo = self._validar_codigo(codigo)
        self.tipo = self._validar_tipo(tipo)
        self.precio = self._validar_precio(precio)
        self.disponibles = self._validar_disponibles(disponibles)

    def _validar_codigo(self, codigo):
        if codigo <= 0:
            raise ValueError("El código debe ser mayor que cero.")
        return codigo

    def _validar_tipo(self, tipo):
        if not tipo or not tipo.strip():
            raise ValueError("El tipo de habitación no puede estar vacío.")
        return tipo.strip()

    def _validar_precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        return float(precio)

    def _validar_disponibles(self, disponibles):
        if disponibles < 0:
            raise ValueError("Las habitaciones disponibles no pueden ser negativas.")
        return disponibles

    def reservar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if cantidad > self.disponibles:
            raise ValueError(f"Error: solo hay {self.disponibles} habitaciones.")
        self.disponibles -= cantidad
        return True

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
        raise ValueError("Error: no existe ese código.")

    def registrar(self, tipo, precio, disponibles):
        nuevo_codigo = len(self.habitaciones) + 1
        nueva_habitacion = TipoHabitacion(nuevo_codigo, tipo, precio, disponibles)
        self.habitaciones.append(nueva_habitacion)
        return nueva_habitacion

    def operar_reserva(self, codigo, cantidad):
        habitacion = self.buscar(codigo)
        habitacion.reservar(cantidad)
        return habitacion