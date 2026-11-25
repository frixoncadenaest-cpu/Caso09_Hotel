class ControladorTienda:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        opcion=""
        while opcion !="4":
            opcion=self.vista()