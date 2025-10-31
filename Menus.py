
from Usuarios import IniciarSesion 
from funciones_cine import ReservaDeButacas

def MenuUser(Usuario):
    while True:
        print("1. revisar la cartelera \n 2. reservar un asiento \n 3. cerrar sesion  ")
        try:
            op=int(input("seleccione la opcion que quiere"))
            if op < 1 and op >3:
                raise ValueError
        except ValueError:
            print("ingrese Un numero que este en las opciones")
        else:    
            if op == 1:
                RevisarLaCartelera()
            if op == 2:
                ReservaDeButacas()#hay que seleccionar la sala 
            if op == 3:                
                break
    return



def MenuAdmin(Usuario):
    while True:
        print("1. revisar las solicitudes de desbloqueo \n 2. revisar el stock de la comida \n 3. Cambiar Precios Del candyBar \n 4. ver datos del Dia   \n 5. cerrar sesion  ")
        try:
            op=int(input("seleccione la opcion que quiere"))
            if op < 1 and op >5:
                raise ValueError
        except ValueError:
            print("ingrese Un numero que este en las opciones")
        else:
            if op == 1:
                SolicitudDeDesbloqueo()
            if op == 2:
                RevisarStock()
            if op == 3:
                CambiarPreciosDelCandy()
            if op == 4:
                VerDatos()
            if op == 5:
                break
    return


def MenuSuperAdmin(Usuario):
    while True:
        print("1. cambiar roles de usuarios \n 2. Simular Datos \n 3. cerrar sesion")
        try:
            op=int(input("seleccione la opcion que quiere"))
            if op < 1 and op >2:
                raise ValueError
        except ValueError:
            print("ingrese Un numero que este en las opciones")
        else:    
            if op == 1:
                CambiarRoles()
            if op == 2:
                SimularDatos()
            if op == 3:
                break
    return

def MenuGuest(Usuario):
    print("1. VerLaspeliculas \n 2.Iniciar Sesion \n 3.Crear cuenta")
    while True:
        try:
            op=int(input("seleccione la opcion que quiere"))
            if op < 1 and op >2:
                raise ValueError
        except ValueError:
            print("ingrese Un numero que este en las opciones")
        else:    
            if op == 1:
                Verlaspeliculas()
            if op == 2:
                IniciarSesion()
            if op == 3:
                CrearCuenta()
