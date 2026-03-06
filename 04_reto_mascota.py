class MascotaVirtual:
    def __init__(self, nombre: str, energia: int =10):
        self.nombre: str = nombre
        self.energia: int = energia
    def jugar(self) -> None:
        self.energia -=3
        print(f"Estado actual de {self.nombre} es: {self.energia}")
    def dormir(self) -> None:
        self.energia +=5
        print(f"Estado actual de {self.nombre} es: {self.energia}")

   
Mascota1 = MascotaVirtual("Ronaldinho")
Mascota1.jugar()
Mascota1.jugar()
Mascota1.jugar()
Mascota1.dormir()
