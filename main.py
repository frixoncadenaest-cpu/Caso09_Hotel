from controlador import ControladorHotel
from modelo import GestorHabitaciones
from vista import VistaHotel


def main():
    modelo = GestorHabitaciones()
    vista = VistaHotel()
    controlador = ControladorHotel(modelo, vista)
    controlador.ejecutar()


if __name__ == "__main__":
    main()