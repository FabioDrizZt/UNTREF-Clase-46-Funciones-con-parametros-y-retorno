try:
    numero = int(input("Ingresa un numero: "))
    print(f"numero ingresado: {numero}")
except ValueError:
    print("Error: debe ingresar un valor numerico")

try:
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    resultado = numerador/denominador
    print(f"Resultado de la división: {resultado}")
except ZeroDivisionError:
    print(f"Error: se intentó dividir por cero.")
except KeyboardInterrupt:
    print(f"Adios vaquero.")
else:
    print("Numeros ingresados de forma valida")
# finally:
#     print("Cerrando todos los recursos antes de finalizar el programa")

# class ErrorNumeroNegativo(Exception):
#     pass

# try:
#     calculo_salario_anual = int(input("Ingrese su sueldo mensual: ")) * 12
#     if calculo_salario_anual < 0:
#         raise ErrorNumeroNegativo("Se ingreso un numero negativo")
# except ErrorNumeroNegativo as err:
#     print(f"Error: {err}")

try:
    calculo_salario_anual = int(input("Ingrese su sueldo mensual: ")) * 12
    if calculo_salario_anual < 0:
        raise ValueError("Se ingreso un numero negativo")
except ValueError as err:
    print(f"Error: {err}")