idProducto = "Numero de identificacion del producto"
tipoProducto = "Tipo de producto"
unidadesExistentes = "Cantidad de unidades disponibles"
precioUnitario = "Precio por unidad del producto"

idProducto = int(input)("Ingrese el numero de identificacion del producto: ")
tipoProducto = input("Ingrese el tipo de producto: ")
unidadesExistentes = int(input)("Ingrese la cantidad de unidades disponibles: ")
precioUnitario = int(input)("Ingrese el precio por unidad del producto: ")

print("El numero de identificacion del producto es", idProducto)
print("El tipo de producto es", tipoProducto)
print("La cantidad de unidades disponibles es", unidadesExistentes)
print("El precio por unidad del producto es", precioUnitario)

if unidadesExistentes >= 0: 
    print("Hay unidades disponibles de este producto")
else: 
    print("No hay unidades disponibles de este producto")
