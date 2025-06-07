from dispositivo import listar, buscar_dispositivos, agregar, eliminar
from automatizaciones import encender, encender_luz_cocina_cafetera, apagar

def main():

    while True:
        print("""
            1. Lista de dispositivos
            2. Buscar dispositivo
            3. Agregar de dispositivos  
            4. Eliminar dispositivo
            5. Encender un dispositivo
            6. Apagar un dispositivo
            7. Encender cafetera y luz de cocina
            8. Salir
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
                nombre = input("Ingrese dispositivo  encender: ").lower()
                print(encender(nombre))

            case "6":
                nombre = input("Ingrese dispositivo a apagar: ").lower()
                print(apagar(nombre))

            case "7":
                encender_luz_cocina_cafetera()
           
            case "8":
                 break

            case _:
                print("Opcion no valida. Intente nuevamente")


if __name__ == "__main__":
    main()