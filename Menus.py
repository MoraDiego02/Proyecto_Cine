from Usuarios import 


def MenuUser(Usuario):
    print("1. revisar la cartelera \n 2. reservar un asiento \n 3   \n 5. cerrar sesion  ")

def MenuAdmin(Usuario):
    print("1. revisar las solicitudes de desbloqueo \n 2. revisar el stock de la comida \n 3. Cambiar Precios Del candyBar 4. ver datos del Dia   \n 5. cerrar sesion  ")

def MenuSuperAdmin(Usuario):
    print("1. cambiar roles de usuarios \n 2. cerrar sesion")
    try:
        op=int(input("seleccione la opcion que quiere"))
        if op < 1 and op >2:
            raise ValueError
    except ValueError:
        print("ingrese Un numero que este en las opciones")
        if op == 1:
            CambiarRoles()
        else:
            return False


def MenuGuest(Usuario):
    print("1. Comprar una entrada \n 2.Iniciar Sesion \n 3.Crear cuenta \n 4. Salir")