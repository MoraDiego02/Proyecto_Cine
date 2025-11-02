from Usuarios import CrearCuenta,IniciarSesion,VerificarRoleDeUsuario
from funciones_cine import CargarSucursales,ReservaDeButacas,SeleccionarSucursal
from logs import EnviarMensajeAAC,SolicitudDeDesbloqueo

def menuprincipal(sucursales):
    while True:
        print("1. Crear Cuenta \n2. IniciarSesion")
        try:
            Opcion=int(input("ingrese el numero de la opcion que quiere: "))
            if Opcion < 1 or Opcion > 2 :
                raise ValueError
        except ValueError:
                print("ingrese un numero que este en las opciones")
        else:
            if Opcion == 1:
                CrearCuenta()
                continue
            else:
                Usuario=IniciarSesion()
                break
    Role=VerificarRoleDeUsuario(Usuario)

    if Role == "User":
        MenuUser(Usuario,sucursales)
    if Role == "Admin":
        MenuAdmin(Usuario,sucursales)
    if Role == "SuperAdmin":
        MenuSuperAdmin(Usuario,sucursales) 

def MenuUser(Usuario,sucursales):
    while True:
        print("1. Comprar un ticket \n2. atencion al cliente\n3. cerrar sesion  ")
        try:
            op=int(input("seleccione la opcion que quiere"))
            if op < 1 and op >3:
                raise ValueError
        except ValueError:
            print("ingrese Un numero que este en las opciones")
        else:                    
            if op == 1:
                SeleccionarSucursal(sucursales)#hay que seleccionar la sala 
            if op == 2:                
                EnviarMensajeAAC(Usuario)
            if op == 3:                
                break
    menuprincipal(sucursales)

def MenuAdmin(Usuario,sucursales):
    while True:
        print()
        print("1. revisar las solicitudes de desbloqueo \n2. revisar el stock de la comida \n3. Cambiar Precios Del candyBar \n4. ver datos del Dia   \n5. cerrar sesion  ")
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
            #if op == 4:
                #VerDatos()
            if op == 5:
                break
    menuprincipal(sucursales)

def MenuSuperAdmin(Usuario,sucursales):
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
    menuprincipal(sucursales)

def main():
    Sucursales=CargarSucursales()
    menuprincipal(Sucursales)
    

if __name__ == "__main__":
    
    main()