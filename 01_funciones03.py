def calcular_area_rectangulo(base: float, altura: float) -> float:
    area: float = base * altura
    return area
medidas: float = calcular_area_rectangulo(5,2)    
print(f"El area del rectangulo es: {medidas}")
