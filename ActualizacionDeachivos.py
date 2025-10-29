from Usuarios import IniciarSesion,EnviarMensajeAAC,SeguridadDeContraseña
from Menus import MenuUser,MenuAdmin, MenuGuest,MenuSuperAdmin


def IngresoDeUsuarios(Info,Op):
    if Op == 1 :#este es para añadir el usuario a la base de datos 
        arch=open("cuentas.cvs",mode="at")
        arch.write(Info)
        arch.close()

def VerificarRoleDeUsuario(Cuenta):
    Role=["User,Admin,SuperAdmin"]
    arch=open("cuentas.cvs",mode="rt")
    
    if Cuenta[len(Cuenta)-1] == Role[0]:
        MenuUser(Cuenta)
    if Cuenta[len(Cuenta)-1] == Role[1]:
        MenuAdmin(Cuenta)
    if Cuenta[len(Cuenta)-1] == Role[2]:
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

def reinicioDeContraseña():
    print("poder autentificar que la cuenta es suya vamos a pedir los siguientes datos")
    arch = open("cuentas.cvs", mode="rt")
    Cuenta = False
    try:
        Usuario = input("ingrese el numero de usuario")
        for linea in arch:
            CuentaAux = linea.strip().split("/")
            if Usuario == CuentaAux[0]:
                Cuenta = CuentaAux
        if Cuenta == False:
            raise ValueError
    except ValueError:
        print("ese nombre de usuario no pertenece a ninguna cuenta")
        
    Errores = 3    
    try:
        Dni = input("ingrese su Dni")

        if Dni == Cuenta [2] :
            print("el Dni es valido")
        else:
            raise ValueError
    except ValueError:
        print("el Dni no es valido")
        Errores -= 1


        if Errores == 0:
            print("se a quedado sin intentos mande un mensaje a atencion al cliente")
            print("1. Si 2. No")
            try:
                op=int(input("seleccione la opcion que quiere"))
                if op < 1 and op > 2:
                    raise ValueError
            except ValueError:
                print("ingrese Un numero que este en las opciones")
                if op == 1:
                    op=EnviarMensajeAAC()
                if op == 2:
                    return 
        
        
    NuevaContraseña = SeguridadDeContraseña()
    Cuenta[1] = NuevaContraseña
   
    arch = open("cuentas.cvs", mode="r", encoding="utf-8")

    LineasActualizadas = []  

    for linea in arch:
        datos = linea.strip().split("/")
        if datos[0] == Usuario:
            nueva_linea = "/".join(Cuenta) + "\n"
            LineasActualizadas.append(nueva_linea)
        
        else:    
            LineasActualizadas.append(linea)

    arch.close()

    arch = open("cuentas.cvs", mode="w", encoding="utf-8")

    for linea in LineasActualizadas:
        arch.write(linea)

    arch.close()

    print("✅ Contraseña actualizada correctamente.")
        

            

    print("el dni que ingreso no pertenece a la cuenta")
    Errores-=1
    print("cuando se acaben los intentos se bloqueara la cuenta y tendra que mandar un mensaje a atencion al cliente")
    print(f" quedan intentos {Errores} fallidos ")

    Contraseña=("ingrese la contraseña: ")

    arch=open("cuentas.cvs", mode="rt")
    for linea in arch:
        aux+=[linea]
    arch.close()


    arch=open("cuentas.cvs", mode="wt")        

    arch.write(aux)


    IniciarSesion()
    
"""   
def cambioContrasena(usuario):
    try
        intentos = 3
        log("ajusteUsuario", "INFO", "Iniciando proceso de cambio contraseña.")
        exContrasena = input("Ingrese su contraseña actual: ").strip()
        while intentos != 0:
            intentos -= 1
            if validarContrasena(usuario,exContrasena) == None:
                log("ajusteUsuario", "WARNING", f"Contraseña antigua incorrecta, quedan {intentos} intento/s.")
                print(f"Contraseña incorrecta, le quedan {intentos} intento/s ")
                exContrasena = input("Ingrese su contraseña actual: ").strip()
            else:
                break
        log("ajusteUsuario", "INFO", "Contraseña antigua correcta.") 
        while True:
            contrasenaNueva = input("Ingrese su nueva contraseña: ")"""



    