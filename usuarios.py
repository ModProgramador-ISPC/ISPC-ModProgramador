from datos import lista_usuarios

def registrar_usuario():
    nombre = input("Ingrese nombre completo: ")
    usuario = input("Ingrese nombre de usuario: ").lower()
    contraseña = input("Ingrese contraseña: ")

    # Si es el primer usuario, será admin
    rol = "admin" if len(lista_usuarios) == 0 else "estandar"

    for u in lista_usuarios:
        if u["usuario"] == usuario:
            print("El nombre de usuario ya está registrado.")
            return None

    nuevo_usuario = {
        "nombre": nombre,
        "usuario": usuario,
        "contraseña": contraseña,
        "rol": rol
    }
    lista_usuarios.append(nuevo_usuario)
    print(f"Usuario registrado con éxito. Rol asignado: {rol}")
    return nuevo_usuario

def iniciar_sesion():
    usuario = input("Usuario: ").lower()
    contraseña = input("Contraseña: ")
    
    for u in lista_usuarios:
        if u["usuario"] == usuario and u["contraseña"] == contraseña:
            print(f"Bienvenido {u['nombre']} ({u['rol']})")
            return u
    print("Credenciales inválidas.")
    return None

def consultar_datos_personales(usuario):
    print("=== Datos personales ===")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Usuario: {usuario['usuario']}")
    print(f"Rol: {usuario['rol']}")

def cambiar_rol():
    if not lista_usuarios:
        print("No hay usuarios registrados.")
        return

    print("=== Lista de usuarios ===")
    for i, u in enumerate(lista_usuarios):
        print(f"{i + 1}. {u['usuario']} - Rol actual: {u['rol']}")

    try:
        seleccion = int(input("Seleccione el número del usuario al que desea cambiar el rol: "))
        if 1 <= seleccion <= len(lista_usuarios):
            usuario = lista_usuarios[seleccion - 1]
            if usuario["rol"] == "admin":
                cantidad_admins = sum(1 for u in lista_usuarios if u["rol"] == "admin")
                if cantidad_admins == 1:
                    print("No se puede cambiar el rol del último administrador.")
                    return

            nuevo_rol = input(f"Ingrese nuevo rol para '{usuario['usuario']}' (admin / estandar): ").lower()
            if nuevo_rol in ["admin", "estandar"]:
                usuario["rol"] = nuevo_rol
                print(f"Rol de {usuario['usuario']} actualizado a {nuevo_rol}.")
            else:
                print("Rol inválido. Debe ser 'admin' o 'estandar'.")
        else:
            print("Selección fuera de rango.")
    except ValueError:
        print("Debe ingresar un número válido.")