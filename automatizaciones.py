from datos import lista_dispositivos

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


