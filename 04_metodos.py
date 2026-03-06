class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular: str = titular
        self.saldo: float = saldo_inicial
    def depositar(self, cantidad: float) -> None:
        self.saldo += cantidad
        print(f"Depósito exitoso. Saldo actual de {self.titular} es: {self.saldo}")
    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            print(f"Saldo de {self.titular} es insuficiente")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual de {self.titular} es: {self.saldo}")
cuenta_ana = CuentaBancaria("Ana", 50000.0)
cuenta_ana.depositar(20000.0)                
cuenta_ana.retirar(100000.0)        
cuenta_ana.retirar(10000.0)    

   