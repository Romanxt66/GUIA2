def es_mayor_edad(edad: int) -> bool:
    if edad >= 18:
        return "Si"
    else:
        return False


usuario1:bool =es_mayor_edad(25)
print(f"El usuario es mayor de edad?: {usuario1}")