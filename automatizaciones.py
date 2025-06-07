from datos import *

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

def cambiar_estado_dispositivos(parametros, opcion_estado):
    #objetivos = ["luz-cocina", "cafetera"]
    estado = False
    if opcion_estado == "1":
        estado = True
    encontrados = []
    no_encontrados = []
    for nombre in parametros:
        resultado = cambiar_estado(nombre, estado)
        if "no se encuentra" in resultado:
            no_encontrados.append(nombre)
        else:
            encontrados.append(nombre)

    if encontrados:
        print(f"Se {"encendieron" if estado else "apagaron"}: {', '.join(encontrados)}")
    if no_encontrados:
        print(f"No se encontraron: {', '.join(no_encontrados)}")

def cargar_automatizaciones(usuario):
    resultado = list(filter(lambda x: x["nombreUsuario"] == usuario, lista_automatizaciones))

    cantidad = len(resultado)
    return cantidad, resultado

def agregar_automatizacion(grupo_dispositivo, dispositivos, usuario):
    nombres_dispositivos = limpiar_datos(dispositivos)

    if len(grupo_dispositivo.strip()) >= 1 and len(nombres_dispositivos) > 1:
        lista_automatizaciones.append(  {
            "nombreUsuario": usuario,
            "nombreGrupo": grupo_dispositivo,
            "parametros": nombres_dispositivos
        })
        return f"Se agrego grupo: {grupo_dispositivo}, disp: {', '.join(nombres_dispositivos)}"
    return "Falta el nombre del grupo o no hay dos o mas dispositivos"

def limpiar_datos(dispositivos):
    lista = dispositivos.split()
    lista_numeros = list(filter(lambda x: x.isdigit(), lista))
    convertir_numero = []
    for numero in lista_numeros:
        convertir_numero.append(int(numero))
    dentro_rango = list(filter(lambda x: 0 < x <= len(lista_dispositivos), convertir_numero))
    eliminar_duplicado = set(dentro_rango)
    restar_uno = [x - 1 for x in eliminar_duplicado]
    nombre_dispositivos = []
    for i, nombre in enumerate(lista_dispositivos):
        if i  in restar_uno:
            nombre_dispositivos.append(nombre["nombre"])
    return nombre_dispositivos