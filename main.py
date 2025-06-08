from dispositivo import listar, buscar_dispositivos, agregar, eliminar
from automatizaciones import activar_modo_noche, encender_luz_cocina_cafetera, apagar_dispositivos_al_salir, simular_ejecutar_automatizacion_log, apagar, consultar_automatizaciones_activas, encender, activar_automatizacion_estandar
from usuarios import (
    registrar_usuario,
    iniciar_sesion,
    consultar_datos_personales,
    cambiar_rol
)
from datos import lista_automatizaciones

def menu_usuario_estandar(usuario):
    while True:
        print("""
        MENÚ USUARIO ESTÁNDAR
        1. Consultar datos personales
        2. Activar automatización
        3. Desactivar automatización
        4. Consultar dispositivos
        5. Cerrar sesión
        """)
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                consultar_datos_personales(usuario)
            case "2":
                print("AUTOMATIZACIONES DISPONIBLES:")
                for i, auto in enumerate(lista_automatizaciones):
                    print(f"{i + 1}. {auto['nombre']}")
                try:
                    seleccion = int(input("Seleccione una automatización a activar: "))
                    if 1 <= seleccion <= len(lista_automatizaciones):
                        nombre = lista_automatizaciones[seleccion - 1]["nombre"]
                        print(simular_ejecutar_automatizacion_log(usuario["nombre"], nombre))
                    else:
                        print("Selección inválida.")
                except ValueError:
                    print("Debe ingresar un número.")
            case "3":
                activas = [a for a in lista_automatizaciones if a["activa"]]
                if not activas:
                    print("No hay automatizaciones activas.")
                    continue
                print("AUTOMATIZACIONES ACTIVAS:")
                for i, auto in enumerate(activas):
                    print(f"{i + 1}. {auto['nombre']}")
                try:
                    seleccion = int(input("Seleccione una automatización a desactivar: "))
                    if 1 <= seleccion <= len(activas):
                        nombre = activas[seleccion - 1]["nombre"]
                        print(apagar(nombre))
                    else:
                        print("Selección inválida.")
                except ValueError:
                    print("Debe ingresar un número.")
            case "4":
                listar()
            case "5":
                break
            case _:
                print("Opción inválida.")

def menu_admin(usuario):
    while True:
        print("""
        MENÚ ADMINISTRADOR
        1. Consultar automatizaciones activas
        2. Gestionar dispositivos
        3. Modificar rol de usuario
        4. Cerrar sesión de modo administrador
        """)
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                activas = consultar_automatizaciones_activas()
                if not activas:
                    print("No hay automatizaciones activas.")
                else:
                    print("AUTOMATIZACIONES ACTIVAS:")
                    for a in activas:
                        print(f"- {a['nombre']}")
            case "2":
                menu_gestion_dispositivos()
            case "3":
                cambiar_rol()
            case "4":
                break
            case _:
                print("Opción inválida.")

def menu_gestion_dispositivos():
    while True:
        print("""
        GESTIÓN DE DISPOSITIVOS
        1. Listar
        2. Buscar
        3. Agregar
        4. Eliminar
        5. Encender
        6. Apagar
        7. Volver
        """)
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                listar()
            case "2":
                nombre = input("Ingrese dispositivo a buscar: ").lower()
                print(buscar_dispositivos(nombre))
            case "3":
                nombre = input("Agregue dispositivo: ").lower()
                print(agregar(nombre))
            case "4":
                nombre = input("Ingrese nombre de dispositivo a eliminar: ").lower()
                print(eliminar(nombre))
            case "5":
                nombre = input("Ingrese dispositivo a encender: ").lower()
                print(encender(nombre))
            case "6":
                nombre = input("Ingrese dispositivo a apagar: ").lower()
                print(apagar(nombre))
            case "7":
                break
            case _:
                print("Opción inválida.")


def main():
    while True:
        print("""
        BIENVENIDO A SMART HOME SOLUTIONS
        1. Registrar nuevo usuario
        2. Iniciar sesión
        3. Salir
        """)
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                registrar_usuario()
            case "2":
                usuario = iniciar_sesion()
                if usuario:
                    if usuario["rol"] == "admin":
                        while True:
                            print("""
                            ¿Cómo desea operar?
                            1. Modo administrador
                            2. Modo usuario estándar
                            3. Cerrar sesión
                            """)
                            modo = input("Seleccione una opción: ")
                            match modo:
                                case "1":
                                    menu_admin(usuario)
                                case "2":
                                    menu_usuario_estandar(usuario)
                                case "3":
                                    break
                                case _:
                                    print("Opción inválida.")
                    else:
                        menu_usuario_estandar(usuario)
            case "3":
                print("Gracias por usar Smart Home Solutions. ¡Hasta luego!")
                break
            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    main()