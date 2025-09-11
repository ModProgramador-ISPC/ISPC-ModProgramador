from datos import lista_automatizaciones, lista_dispositivos

def simular_ejecutar_automatizacion_log(nombre_usuario, automatizacion_nombre):
    mensaje = f"☕ Automatización '{automatizacion_nombre}' ejecutada por {nombre_usuario}."
    print("✅", mensaje)
    return mensaje

def consultar_automatizaciones_activas():
    activas = [a for a in lista_automatizaciones if a.get("activa", False)]
    print("\n--- Automatizaciones Activas (Solo Admin) ---")
    if not activas:
        print("No hay automatizaciones activas en este momento.")
    else:
        for i, auto in enumerate(activas):
            print(f"{i + 1}. {auto['nombre']} - Descripción: {auto.get('descripcion', 'Sin descripción')}")
    return activas    

def activar_automatizacion_estandar(usuario):
    print("\n--- Automatizaciones Disponibles para Ejecutar ---")
    if not lista_automatizaciones:
        print("No hay automatizaciones predefinidas disponibles.")
        return

    for i, auto in enumerate(lista_automatizaciones):
        estado_activa = "(Activa por defecto)" if auto.get("activa", False) else "(Inactiva por defecto)"
        print(f"{i + 1}. {auto['nombre']} {estado_activa} - {auto.get('descripcion', 'Sin descripción')}")

    try:
        seleccion = int(input("Seleccione el número de la automatización a ejecutar (0 para cancelar): "))
        if seleccion == 0:
            print("Ejecución de automatización cancelada.")
            return

        if 1 <= seleccion <= len(lista_automatizaciones):
            automatizacion_seleccionada = lista_automatizaciones[seleccion - 1]
            simular_ejecutar_automatizacion_log(usuario['nombre'], automatizacion_seleccionada['nombre'])
            automatizacion_seleccionada["activa"] = True
            if automatizacion_seleccionada["funcion_asociada"] == "encender_luz_cocina_cafetera":
                encender_luz_cocina_cafetera()
            elif automatizacion_seleccionada["funcion_asociada"] == "apagar_dispositivos_al_salir":
                apagar_dispositivos_al_salir()
            elif automatizacion_seleccionada["funcion_asociada"] == "activar_modo_noche":
                activar_modo_noche()
            else:
                print(f"✅ Automatización '{automatizacion_seleccionada['nombre']}' predefinida simulada para ejecución.")

        else:
            print("⚠️ Selección inválida. Por favor, ingrese un número de la lista.")
    except ValueError:
        print("⚠️ Entrada inválida. Por favor, ingrese un número.")

def cambiar_estado(dispositivo, estado):
    for i, diccionario in enumerate(lista_dispositivos):
        if dispositivo == diccionario["nombre"].lower():
            lista_dispositivos[i]["estado"] = estado
            accion = "encendió" if estado else "apagó"
            return f"El dispositivo {dispositivo} se {accion}."
    return f"El dispositivo {dispositivo} no se encuentra."

def encender(dispositivo):
    return cambiar_estado(dispositivo, True)

def apagar(dispositivo):
    return cambiar_estado(dispositivo, False)

def encender_luz_cocina_cafetera():
    objetivos = ["luz-cocina", "cafetera"]
    encontrados = []
    no_encontrados = []

    for nombre in objetivos:
        resultado = cambiar_estado(nombre, True)
        if "no se encuentra" in resultado:
            no_encontrados.append(nombre)
        else:
            encontrados.append(nombre)

    if encontrados:
        print(f"Se encendieron: {', '.join(encontrados)}")
    if no_encontrados:
        print(f"No se encontraron: {', '.join(no_encontrados)}")

def apagar_dispositivos_al_salir():
    print("🌙 Todos los dispositivos principales apagados.")
    for disp in lista_dispositivos:
        if disp["estado"]: 
            print(apagar(disp["nombre"])) 
    print("------------------------------------")

def activar_modo_noche():
    print("😴 Modo Noche activado. Luces tenues.")
    print("----------------------------")    


def activar_automatizacion(nombre):
    for auto in lista_automatizaciones:
        if auto["nombre"].lower() == nombre.lower():
            auto["activa"] = True
            return f"La automatización '{nombre}' fue activada."
    return f"No se encontró la automatización '{nombre}'."

def desactivar_automatizacion(nombre):
    for auto in lista_automatizaciones:
        if auto["nombre"].lower() == nombre.lower():
            auto["activa"] = False
            return f"La automatización '{nombre}' fue desactivada."
    return f"No se encontró la automatización '{nombre}'."
