from datos import lista_dispositivos


def listar ():
    for i, dispositivo in enumerate(lista_dispositivos):
         print(f"{i + 1}. {dispositivo["nombre"]}")
        

def buscar_dispositivos(dispositivo):
       for diccionario in lista_dispositivos:
           if diccionario["nombre"] == dispositivo:
               return f"Se encontro el dispositivo {dispositivo} de la marca: {diccionario["marca"]}, modelo: {diccionario["modelo"]}, ubicación: {diccionario["ubicacion"]}, y su estado es {"encendido" if diccionario["estado"] else "apagado" }"

       return f"No se encontro el dispositivo {dispositivo}"
    
def agregar(dispositivo, ubicacion, modelo, marca):
    if modelo == "":
        modelo = "no tiene"

    if marca == "":
        marca = "no tiene"

    for diccionario in lista_dispositivos:
        if dispositivo == diccionario["nombre"]:
            return f"El dispositivo {dispositivo} ya existe."
    lista_dispositivos.append({"nombre":dispositivo, "estado": False, "ubicacion": ubicacion, "modelo": modelo, "marca": marca})
    return f"El dispositivo {dispositivo} ha sido agregado exitosamente."


def eliminar(dispositivo):
    for i, diccionario in enumerate(lista_dispositivos):
        if diccionario["nombre"] == dispositivo:
            lista_dispositivos.pop(i)
            return f"Se encontro el dispositivo {dispositivo} y se eliminó"

    return f"No se encontro el dispositivo {dispositivo}"

