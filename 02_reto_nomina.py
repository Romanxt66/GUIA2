def calcular_salario_neto(salario_base: float, bonificacion: float= 0.0) -> float:
    return salario_base + bonificacion - (salario_base * 0.08)
salario_neto: float = calcular_salario_neto(1765000)
print(f"El salario neto es : {salario_neto}")
    