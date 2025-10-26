from Usuarios import IniciarSesion


def IngresoDeUsuarios(Info,Op):
    if Op == 1 :#este es para añadir el usuario a la base de datos 
        arch=open("cuentas.cvs",mode="at")
        arch.write(Info)
        arch.close()
        


def EncontrarUsuario(Info):
        arch=open("cuentas.cvs",mode="rt")
        Cuenta=False
        for linea in arch:
            CuentaAux=linea.strip().split("/")
            if Info == CuentaAux[0]:
                Cuenta=CuentaAux
        arch.close()
        return Cuenta

def reinicioDeContraseña():
    print("poder autentificar que la cuenta es suya vamos a pedir los siguientes datos")
    arch=open("cuentas.cvs", mode="rt")
    Cuenta=False
    try:
        Usuario=input("ingrese el numero de usuario")
        for linea in arch:
            CuentaAux=linea.strip().split("/")
            if Usuario == CuentaAux[0]:
                Cuenta=CuentaAux
        if Cuenta == False:
            ValueError
    except ValueError:
        print("ese nombre de usuario no pertenece a ninguna cuenta")
        
    Errores=3    
    try:

        Dni=int(input("ingrese su Dni:"))
        if Dni == Cuenta [2] :
            print("el Dni es valido")


        if Errores == 0:
            print(" quiere seguir intentando")
            print("Si o No")
            opcion=input("escriba la opcion que quiere: ")

            
    except ValueError:
        print("el dni que ingreso no pertenece a la cuenta")
        Errores-=1
        print(f" quedan intentos {Errores} fallidos ")


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



    