color = "naranja"

match color:
    case "rojo":
        print("Toco un 10% de descuento")
    case "azul":
        print("Toco un 25% de descuento")
    case _:
        print("Color invalido")

dia_semana = "jueves"

match dia_semana:
    case "lunes" | "martes" | "miercoles":
        print("es un dia laboral")
    case "jueves" | "viernes":
        print("Hoy es Juernes ! 🎉 ")
    case "sabado" | "domingo":
        print("Es finde !")

numero = 42

match numero:
    case n if n<0:
        print("el numero es negativo")
    case n if n>0:
        print("el numero es positivo")
    case _:
        print("No es ni positivo ni negativo")