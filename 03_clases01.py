class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca: str= marca
        self. modelo: str = modelo
        self.anio: int = anio


Vehiculo1 = Vehiculo("Toyota", "Corolla", 2022)
Vehiculo2 = Vehiculo("Honda", "Civic", 2023)


print(f"El vehiculo {Vehiculo1.marca} {Vehiculo1.modelo} {Vehiculo1.anio}")
print(f"El vehiculo {Vehiculo2.marca} {Vehiculo2.modelo} {Vehiculo2.anio}")
        