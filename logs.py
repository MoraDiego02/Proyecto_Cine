from datetime import datetime 


def log (FFuncion, Typ0, Usuario):
    fecha=datetime.now()
    fecha=fecha.strftime("%d/%m/%Y %H:%M:%S")
    print(fecha)
    TiposDeReport=("CambioDeRol","SolicitudDeReponerStock","SolicitudDeDesbloqueoDecuenta","reinicioDecontraseña")
    Report=TiposDeReport[Typ0]
    with open("log.txt", mode="a" ,encoding="utf-8") as arch:
        ReporteCompleto=(f"{fecha} {Report} from {FFuncion} By {Usuario} ")
        arch.write(ReporteCompleto)
    

def EnviarMensajeAAC(Opcion):

    with open("Mensajes/Solicitudes.cvs",mode="at") as Arch:

        print("bienvenido a atencion al cliente")
        print("ingrese el tipo de mensaje que quiere enviar")
        while Opcion!=2:
            print("1.segurencia 2.Solicitud De reinicio de contraseña ")
    
            MENS=input("")
            Mensaje=print("ingrese el mensajes:")

            print("desea mandar otro mensaje")
            print("1. enviar otro mensaje 2. para salir ")
            Opcion=int(input("ingrese su seleccion: "))

        return Opcion




def SolicitudDeDesbloqueo():
    arch=open("Mensajes/Solicitudes.cvs",mode="at")
    for lineas in arch:
        print(lineas)
        
        