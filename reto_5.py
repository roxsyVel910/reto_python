def new_user(usuarios, ids, num):
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

def show_user(usuarios, id_usuario):
    if id_usuario in usuarios:
        print(f"Información del usuario con ID {id_usuario}:")
        print(f"Nombre: {usuarios[id_usuario]['nombre']}")
        print(f"Apellidos: {usuarios[id_usuario]['apellidos']}")
        print(f"Correo: {usuarios[id_usuario]['correo']}")
        print(f"Teléfono: {usuarios[id_usuario]['telefono']}")
    else:
        print("ID de usuario no válido")

def edit_user(usuarios, id_usuario):
    if id_usuario in usuarios:
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

        usuarios[id_usuario] = {'nombre': nombre, 'apellidos': apellidos, 'correo': correo, 'telefono': telefono}
        print("Información actualizada correctamente")
    else:
        print("ID de usuario no válido")

def delete_user(usuarios, ids, id_usuario):
    if id_usuario in usuarios:
        del usuarios[id_usuario]
        ids.remove(id_usuario)
        print("Usuario eliminado correctamente")
    else:
        print("ID de usuario no válido")

def list_users(ids):
    print("IDs de usuarios registrados:", ids)