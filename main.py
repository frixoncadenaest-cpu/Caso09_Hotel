from modelo import GestorProductos
from vista import VistaTienda
from controlador import ControladorTienda

modelo=GestorProductos()
vista=VistaTienda()
controlador=ControladorTienda(modelo, vista)
controlador.ejecutar()