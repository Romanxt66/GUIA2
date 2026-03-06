class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible: float = 1000.0

    def solicitar_retiro(self) -> None:
        print("Bienvenido al cajero") 
        try:
            monto_str: str = input("Ingrese el monto a retirar (solo numeros)")
            monto: float = float(monto_str)
            if monto == 0:
                raise ValueError("No puede retirar 0 pesos")

            self.efectivo_disponible -= monto
            print(f"Retiro exitoso. Saldo restante: {self.efectivo_disponible}")
        except ValueError as e:
            print(f"Error caracteres invalidos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            print("Gracias por usar el cajero")

            
mi_cajero = CajeroAutomatico()
mi_cajero.solicitar_retiro()
