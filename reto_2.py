
#REto del dia 2

'''programa en Python capaz de registrar un nuevo usuario en el sistema. Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.
Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores: Nombre, apellidos, número de teléfono y correo electrónico. Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.
Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50. Así mismo el número de teléfono será a 10 dígitos. Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos. '''


num = int(input("Ingrese el número de nuevos usuarios a registrar: "))
usuarios = []
for _ in range(num):
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

print("Usuarios registrados correctamente:")
for usuario in usuarios:
    print(f"Nombre: {usuario[0]}, Apellidos: {usuario[1]}, Correo: {usuario[2]}, Teléfono: {usuario[3]}")