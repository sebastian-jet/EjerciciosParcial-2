nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

if nacionalidad == "N":
    print("Usted es Mexicano")
else:
    print("Usted no es Mexicano")