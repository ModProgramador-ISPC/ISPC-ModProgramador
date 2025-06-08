lista_dispositivos = [
    {"nombre": "luz-cocina", "estado": False},
    {"nombre": "cafetera", "estado": False}
]

lista_usuarios = []

lista_automatizaciones = [
    {
        "nombre": "Encender cafetera y luz de cocina al amanecer",
        "funcion_asociada": "encender_luz_cocina_cafetera",
        "activa": True,
        "descripcion": "Enciende automáticamente la cafetera y la luz de la cocina a primera hora."
    },
    {
        "nombre": "Apagar todo al salir",
        "funcion_asociada": "apagar_dispositivos_al_salir",
        "activa": False,
        "descripcion": "Apaga todos los dispositivos cuando el usuario sale de casa."
    },
    {
        "nombre": "Modo Noche (luces tenues)",
        "funcion_asociada": "activar_modo_noche",
        "activa": True,
        "descripcion": "Ajusta las luces a un nivel tenue para el modo noche."
    }
]
