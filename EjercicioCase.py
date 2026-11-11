name = ""
brand = ""
stock = 0
fechaCad = ""
precio = 0
opcion = 0

print("Bienvenido al sistema de registro de articulos")
print("---------MENU PRINCIPAL---------")
print("1. Registrar articulo")
print("2. Ver informacion del articulo")
print("3. Borrar informacion del articulo")
print("4. Modificar informacion del articulo")
print("5. Salir")
print("---------------------------------")
opcion = int(input("Selecciona una opcion: "))

match opcion:#Aqui inicia el match, que es una validacion de caso

    case 1:
        name = input("Ingrese el nombre del articulo: ")
        brand = input("Ingrese la marca del articulo:  ")
        stock = int(input("Ingrese la cantidad de unidades disponibles: "))
        fechaCad = input("Ingrese la fecha de caducidad del articulo: ")
        precio = float(input("Ingrese el precio del articulo: "))
    case 2:
        print("Nombre: ", name, "Marca: ", brand, "Cantidad de unidades disponibles: ", stock, "Fecha de caducidad: ", fechaCad, "Precio: ", precio)
    case 3:
        name = ""
        brand = ""
        stock = 0
        fechaCad = ""
        precio = 0
    case 4:
        name = input("Ingrese el nombre del articulo: ")
        brand = input("Ingrese la marca del articulo:  ")
        stock = int(input("Ingrese la cantidad de unidades disponibles: "))
        fechaCad = input("Ingrese la fecha de caducidad del articulo: ")
        precio = float(input("Ingrese el precio del articulo: "))
    case 5:
        print("¡Hasta luego!")
    case _:
        print("Opcion no valida")