class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.nombre: str = nombre
        self.salario: float = salario
    def trabajar(self) -> None:
        print(f"{self.nombre} esta cumpliendo su horario regular .")

class Desarrollador(Empleado):
    def programador(self) -> None:
        print(f"{self.nombre} esta programando en Python.")

class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esat en una reunion estrategica.")


dev = Desarrollador("Roman", 1000)
jefe = Gerente("Ana", 5000)

dev.trabajar()
dev.programador()
jefe.trabajar()