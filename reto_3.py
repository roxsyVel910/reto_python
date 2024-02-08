
#REto del dia 3

num = int(input("Ingrese el número de nuevos usuarios a registrar: "))
usuarios = []
ids = []

for i in range(1, num + 1):
    nombre = input("Ingrese el nombre: ")
    while len(nombre) < 5 or len(nombre) > 50:
        print("Error: La longitud del nombre debe estar entre 5 y 50 caracteres.")
        nombre = input("Ingrese el nombre: ")

    apellidos = input("Ingrese los apellidos: ")
    while len(apellidos) < 5 or len(apellidos) > 50:
        print("Error: La longitud de los apellidos debe estar entre 5 y 50 caracteres.")
        apellidos = input("Ingrese los apellidos: ")

    correo = input("Ingrese el correo electrónico: ")
    while len(correo) < 5 or len(correo) > 50:
        print("Error: La longitud del correo electrónico debe estar entre 5 y 50 caracteres.")
        correo = input("Ingrese el correo electrónico: ")

    telefono = input("Ingrese el número de teléfono: ")
    while len(telefono) != 10:
        print("Error: El número de teléfono debe tener 10 dígitos.")
        telefono = input("Ingrese el número de teléfono: ")

    usuarios.append((nombre, apellidos, correo, telefono))
    ids.append(i)

print("Usuarios registrados correctamente:")
for i, usuario in zip(ids, usuarios):
    print(f"ID: COD0{i}, Nombre: {usuario[0]}, Apellidos: {usuario[1]}, Correo: {usuario[2]}, Teléfono: {usuario[3]}")