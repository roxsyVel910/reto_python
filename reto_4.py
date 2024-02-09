num = int(input("Ingrese el número de nuevos usuarios a registrar: "))
usuarios = {}
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

    usuarios[i] = {'nombre': nombre, 'apellidos': apellidos, 'correo': correo, 'telefono': telefono}
    ids.append(i)

while True:
    print("Seleccione una opción:")
    print("A - Agregar nuevo usuario")
    print("B - Listar IDs de usuarios")
    print("C - Ver información de un usuario")
    print("D - Editar información de un usuario")
    print("E - Salir")
    opcion = input("Ingrese la letra de la opción deseada: ").upper()

    if opcion == 'A':
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

        usuarios[num + 1] = {'nombre': nombre, 'apellidos': apellidos, 'correo': correo, 'telefono': telefono}
        ids.append(num + 1)
        num += 1

    elif opcion == 'B':
        print("IDs de usuarios registrados:", ids)

    elif opcion == 'C':
        id_usuario = int(input("Ingrese el ID del usuario: "))
        if id_usuario in usuarios:
            print(f"Información del usuario con ID {id_usuario}:")
            print(f"Nombre: {usuarios[id_usuario]['nombre']}")
            print(f"Apellidos: {usuarios[id_usuario]['apellidos']}")
            print(f"Correo: {usuarios[id_usuario]['correo']}")
            print(f"Teléfono: {usuarios[id_usuario]['telefono']}")
        else:
            print("ID de usuario no válido")

    elif opcion == 'D':
        id_usuario = int(input("Ingrese el ID del usuario a editar: "))
        if id_usuario in usuarios:
            nombre = input("Ingrese el nombre: ")
            
            usuarios[id_usuario]['nombre'] = nombre
            apellidos = input("Ingrese los apellidos: ")
          
            usuarios[id_usuario]['apellidos'] = apellidos
            correo = input("Ingrese el correo electrónico: ")

            usuarios[id_usuario]['correo'] = correo
            
            telefono = input("Ingrese el número de teléfono: ")
            while len(telefono) != 10:
             print("Error: El número de teléfono debe tener 10 dígitos.")
            telefono = input("Ingrese el número de teléfono: ")

            usuarios[id_usuario]['telefono'] = telefono
            print("Información actualizada correctamente")
        else:
            print("ID de usuario no válido")

    elif opcion == 'E':
        break

    else:
        print("Opción no válida")