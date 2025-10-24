from ActualizacionDeachivos import AdministrarArchivos
def CrearCuenta():#este es para exportar la cuenta creada a el archivo
    arch=open("cuentas.cvs",mode="at")
    Usuario=NombreDeusuario()
    Contraseña=SeguridadDeContraseña()
    Documento=ComprobacionDeDniYFecha(1)
    Fecha=ComprobacionDeDniYFecha(2)
    Datos=(f"{Usuario}/{Contraseña}/{Documento}/{Fecha}\n")
    arch.write(Datos)
    arch.close
    AdministrarArchivos(Datos,1)
    RegistroDeUsuario(1)
    
    
def IniciarSesion():#esta es para verificar 
    while True:
        try:
            Usuario=input("ingrese su nombre de usuario: ")
            if VerificacionDeDatos(1,Usuario) == False:
                raise ValueError
        except ValueError:
            print("el nombre de usuario que ingreso no es valido")
        else:
            print("el usuario es valido")
            Errores=0
            
            if Errores == 3:
                print("desea reiniciar la contraseña: ")
                print("1. Si 2. No")
                print("ingrese un numero (1 o 2) ")
                Eleccion=int(input("1. Si 2. No"))
                if Eleccion == 1:
                    reinicioDeContraseña()
                else:
                    Errores=0
            else:
                
                try:     
                    contraseña=input("ingrese la contraseña: ")
                    if VerificacionDeDatos(2,contraseña) == False:
                        Errores+=1
                        raise ValueError
                except ValueError:
                    print("la contraseña no es valida")                    
                else:
                    print("se a realizado el logueo de la cuenta con exito!")
                    break


def RegistroDeUsuario(Opcion):
    if Opcion == 1:
       print("Inicio de Sesion")
       Usuario=IniciarSesion() 
                
    else:#este es el que crear las cuentas
        CrearCuenta()
            
    return Usuario
    
def VerificacionDeDatos(OP,Dato):#este va con el de Inicio de sesion
    
    TorF=False ###puto el que lee###
    if OP==1:
        arch=open("cuentas.cvs",mode="rt")
        while True:
            Cuenta=arch.readline().strip().split("/")
            if Dato == Cuenta[0]:
                print(Cuenta[0])
                TorF=True
                print("el usuario es valido")
                arch.close()
                break
        return TorF
    else:
        arch=open("cuentas.cvs",mode="rt")
        while True:
            Cuenta=arch.readline().strip().split("/")
            if Dato == Cuenta[1]:
                TorF=True
                print("la contraseña es valida")
                arch.close()
                break
        return TorF

        

def reinicioDeContraseña(Usuario):#este lo voy a mandar a usuario si pone mas de 3 veces la contraseña
    while True:
        AdministrarArchivos(1)
        break

def SeguridadDeContraseña():#este va a ser el creador de contraseña
    while True:
        Contraseña=input("ingrese la contraseña:")
        try:
            if len(Contraseña)<8:
                raise IndexError
        except IndexError:
            print("la Contraseña es demasiado corta")
            continue
        else:
            try:
                SimbolosNecesarios=["!","_","-","~","@","*","<",">","?"]
                valor=0
                for i in range(len(Contraseña)):
                    if Contraseña[i] in SimbolosNecesarios:
                            valor=1
                    else:
                        continue
                if valor == 0:
                    raise ValueError
            except ValueError:
                print("la contraseña no es suficientemente segura")
            else:
                print("la contraseña es segura")
                break
    return Contraseña


def NombreDeusuario():#este es para verificar de que el nombre de usuario este disponible
    arch=open("cuentas.cvs",mode="rt")
    while True:
        print("el nombre de usuario tiene que tener mas de 8 caracteres")
        try:
            Usuario=input("nombre de usuario:")
            if len(Usuario)<8:
                raise IndexError
            else:
                while AuxUsuario:
                    AuxUsuario=arch.readline()
                    if AuxUsuario == Usuario:
                        ValueError
                    else:
                        continue
                break
    
        except IndexError:
            print("el nombre tiene que tener mas o igual a 8 caracteres")
        except ValueError:
            print("ese nombre de usuario ya esta ocupado por otra persona")
        else:
            print("el nombre es valido")
            break
    arch.close()
    return Usuario
    

def ComprobacionDeDniYFecha(Opcion):
    if Opcion == 1:
        documento=int(input("ingrese su DNI sin puntos:"))
        while True:
            try:
                if documento <10000000 or documento >99999999:
                    raise ValueError
            except ValueError:
                print("el DNI ingresado no es valido")
            else:
                print("el DNI es valido")
                break
        return str(documento)
    else:
        while True:
            try:
                fecha=input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa:")
                dia=int(fecha[0:2])
                mes=int(fecha[3:5])
                año=int(fecha[6:10])
                if dia < 1 or dia > 31 or mes < 1 or mes > 12 or año < 1930 or año > 2025:
                    raise ValueError
            except ValueError:
                print("La fecha de nacimiento es invalida. Volve a intentarlo")
            else:
                print("La fecha de nacimiento es valida")
                break
        fecha=(f"{dia}:{mes}:{año}")
        return fecha

