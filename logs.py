from datetime import datetime 


def log (FFuncion, Typ0, Usuario):
    fecha=datetime.now()
    fecha=fecha.strftime("%d/%m/%Y %H:%M:%S")
    
    TiposDeReport=("CambioDeRol","FinDeldia","reinicioDecontraseña","login","GenerarUsuarios")
    Report=TiposDeReport[Typ0]
    with open("log.txt", mode="a" ,encoding="utf-8") as arch:
        ReporteCompleto=(f"{fecha} {Report} from {FFuncion} By {Usuario} ")
        arch.write(ReporteCompleto)
    

def EnviarMensajeAAC():
    fecha=datetime.now()
    fecha=fecha.strftime("%d/%m/%Y %H:%M:%S")


    print("bienvenido a atencion al cliente")
    print("ingrese el tipo de mensaje que quiere enviar")
    print("1.segurencia 2. quejas")
    typo=["sugerencia","quejas"]
    try:
        Opcion=int(input("ingrese su seleccion: "))
        if Opcion < 1 or Opcion >2:
            raise ValueError
        else:

            Mens=input("ingrese el mensajes: ")

        mensaje=(f"{fecha} {typo[Opcion-1]} {Mens}")
        with open("Mensajes/Solicitudes.csv",mode="at")as arch:
            arch.write(mensaje)

    except ValueError:
        print("la opcion solo puede ser (1 o 2)")
    except (IOError, OSError):
        print("Error al abrir el archivo.")



        