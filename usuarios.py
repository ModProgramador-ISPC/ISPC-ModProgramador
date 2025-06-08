from datos import lista_usuarios

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    telefono = input("Ingrese su número de telefono: ")
    dni = input("Ingrese su DNI: ")
    contraseña = input("Ingrese contraseña: ")

    # Si es el primer usuario, será admin
    rol = "admin" if len(lista_usuarios) == 0 else "estandar"

    for u in lista_usuarios:
        if u["dni"] == dni:
            print("El DNI ya está registrado.")
            return None

    nuevo_usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "telefono": telefono, 
        "contraseña": contraseña,
        "rol": rol
    }
    lista_usuarios.append(nuevo_usuario)
    print(f"Usuario registrado con éxito. Rol asignado: {rol}")
    return nuevo_usuario

def iniciar_sesion():
    dni = input("DNI: ").lower()
    contraseña = input("Contraseña: ")
    
    for u in lista_usuarios:
        if u["dni"] == dni and u["contraseña"] == contraseña:
            print(f"Bienvenido {u['nombre']} {u['apellido']} ({u['rol']})")
            return u
    print("Credenciales inválidas.")
    return None

def consultar_datos_personales(usuario):
    print("=== Datos personales ===")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Apellido: {usuario['apellido']}")
    print(f"Telefono: {usuario['telefono']}")
    print(f"DNI: {usuario['dni']}")
    print(f"Rol: {usuario['rol']}")

def cambiar_rol():
    if not lista_usuarios:
        print("No hay usuarios registrados.")
        return

    print("=== Lista de usuarios ===")
    for i, u in enumerate(lista_usuarios):
        print(f"{i + 1}. {u['dni']} - Rol actual: {u['rol']}")

    try:
        seleccion = int(input("Seleccione el número del usuario al que desea cambiar el rol: "))
        if 1 <= seleccion <= len(lista_usuarios):
            usuario = lista_usuarios[seleccion - 1]
            if usuario["rol"] == "admin":
                cantidad_admins = sum(1 for u in lista_usuarios if u["rol"] == "admin")
                if cantidad_admins == 1:
                    print("No se puede cambiar el rol del último administrador.")
                    return

            nuevo_rol = input(f"Ingrese nuevo rol para '{usuario['dni']}' (admin / estandar): ").lower()
            if nuevo_rol in ["admin", "estandar"]:
                usuario["rol"] = nuevo_rol
                print(f"Rol de {usuario['dni']} actualizado a {nuevo_rol}.")
            else:
                print("Rol inválido. Debe ser 'admin' o 'estandar'.")
        else:
            print("Selección fuera de rango.")
    except ValueError:
        print("Debe ingresar un número válido.")
