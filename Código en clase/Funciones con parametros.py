def convertir_temperatura(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

print(convertir_temperatura(20))

# Para trabajar con listas
def sumar_todos(*args):
    return sum(args)

suma = sumar_todos(1,3,5,7,9)

# para trabajar con diccionarios
def describir_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona(nombre="Fabio", edad=36, profesion="Profesor")