

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
    
    
    print("papapappaappaprararararar")





    