from Menus import MenuUser,MenuAdmin, MenuGuest,MenuSuperAdmin
from logs import log

def VerificarRoleDeUsuario(Cuenta):
    Role=["User,Admin,SuperAdmin"]
    
    if Cuenta[len(Cuenta)] == Role[0]:
        MenuUser(Cuenta)
    if Cuenta[len(Cuenta)] == Role[1]:
        MenuAdmin(Cuenta)
    if Cuenta[len(Cuenta)] == Role[2]:
        MenuSuperAdmin(Cuenta)
    if Cuenta == False:
        MenuGuest(Cuenta)

def CambiarRoles():
    while True:
        arch=open("cuentas.cvs",mode="rt")
        print("ingrese el nombre del usuario al que le quiere cambiar el rol")    
        try:
            Usuario=input("nombre: ")
            Cuenta=EncontrarUsuario(Usuario)
            if Cuenta == False:
                raise ValueError
        except ValueError:
            print("ese usuario no existe")

        try: 
            print("1.Si 2.No")
            Opcion=int(input("quiere seguir:"))
            
            if Opcion < 1 or Opcion > 2:
                raise ValueError 
            
            if Opcion == 1:
                arch.close()
                continue
            
            if Opcion == 2:
                break

        except ValueError:
            print("ingrese un numero (1 o 2) ")
            log("CambiarDeRoles",0,"SuperAdmin")
            return



def EncontrarUsuario(Info):
        arch=open("cuentas.cvs",mode="rt")
        Cuenta=False

        for linea in arch:
            CuentaAux = linea.strip().split("/")
        
            if Info == CuentaAux[0]:
                Cuenta = CuentaAux
        
        arch.close()
        return Cuenta
