def calcular(num_a, num_b, operacion):
    """
    Realiza operaciones matemáticas básicas entre dos números.

    Args:
        num_a (float): Primer número.
        num_b (float): Segundo número.
        operacion (str): Operación a realizar ("suma", "resta", "multiplicacion", "division").

    Returns:
        float | str: Resultado de la operación o un mensaje de error en caso de excepción.
    """
    try:
        # Convertir los parámetros a float por si se reciben como cadenas
        num_a = float(num_a)
        num_b = float(num_b)

        # Realizar la operación usando match
        match operacion:
            case "suma":
                return num_a + num_b
            case "resta":
                return num_a - num_b
            case "multiplicacion":
                return num_a * num_b
            case "division":
                if num_b == 0:
                    raise ZeroDivisionError("La división por cero no está permitida.")
                return num_a / num_b
            case _:
                return "Operación no reconocida. Usa: 'suma', 'resta', 'multiplicacion' o 'division'."
    except ValueError:
        return "Error: Ambos parámetros deben ser números válidos."
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"


print(calcular(10, 5, "suma"))             # Salida: 15.0
print(calcular(10, 5, "resta"))            # Salida: 5.0
print(calcular(10, 5, "multiplicacion"))   # Salida: 50.0
print(calcular(10, 0, "division"))         # Salida: Error: La división por cero no está permitida.
print(calcular(10, "cinco", "suma"))       # Salida: Error: Ambos parámetros deben ser números válidos.
print(calcular(10, 5, "potencia"))         # Salida: Operación no reconocida.