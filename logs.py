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
    