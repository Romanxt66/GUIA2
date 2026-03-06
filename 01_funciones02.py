def calcular_iva(precio_base: float) -> None:
    iva: float = precio_base* 0.19
    precio_final: float = precio_base + iva
  
factura_1: float = calcular_iva(1000)
factura_2: float = calcular_iva(2500)    
print(f"Factura 1: {factura_1}")
print(f"Factura 2: {factura_2}")
  