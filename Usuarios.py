from ActualizacionDeachivos import IngresoDeUsuarios, reinicioDeContraseña,EncontrarUsuario
def CrearCuenta():#este es para exportar la cuenta creada a el archivo
    arch=open("cuentas.cvs",mode="at")
    Usuario=NombreDeusuario()
    Contraseña=SeguridadDeContraseña()
    Documento=ComprobacionDeDniYFecha(1)
    Fecha=ComprobacionDeDniYFecha(2)
    Datos=(f"{Usuario}/{Contraseña}/{Documento}/{Fecha}\n")
    arch.write(Datos)
    arch.close
    IngresoDeUsuarios(Datos)
    RegistroDeUsuario(1)
    
    
def IniciarSesion():
    while True:
        try:
            Usuario=input("ingrese su nombre de usuario: ")
            Cuenta=EncontrarUsuario(Usuario)
            if Cuenta == False:
                raise ValueError
            else:
                break

        except ValueError:
            print("el nombre de usuario que ingreso no es valido")
    Errores=0
    while True:
        if Errores == 3:
            print("desea reiniciar la contraseña: ")
            print("1. Si 2. No")
            
            try:
                Eleccion=int(input("ingrese un numero (1 o 2): "))
                if Eleccion == 1:
                    reinicioDeContraseña()
                else:
                    Errores=0
            except ValueError:
                print("ingrese 1 o 2 porfavor")
        else:
            try:     
                contraseña=input("ingrese la contraseña: ")
                if VerificacionDeContraseña(contraseña,Cuenta[1]) == False:
                    Errores+=1
                    raise ValueError
            except ValueError:
                    print("la contraseña no es valida")                    
            else:
                print("se a realizado el logueo de la cuenta con exito!")
                break
    return Cuenta


def RegistroDeUsuario(Opcion):
    if Opcion == 1:
       print("Inicio de Sesion")
       Usuario=IniciarSesion() 
                
    else:#este es el que crear las cuentas
        CrearCuenta()   
    return Usuario
    
def VerificacionDeContraseña(Cuenta,Contraseña):#este va con el de Inicio de sesion
    TorF=False
    if Contraseña == Cuenta:
        TorF=True
    return TorF

def NombreDeusuario():#este es para verificar de que el nombre de usuario este disponible
    arch=open("cuentas.cvs",mode="rt")
    while True:
        print("el nombre de usuario tiene que tener mas de 8 caracteres")
        try:
            Usuario=input("nombre de usuario:")
            if len(Usuario)<8:
                raise IndexError
            else:
                for linea in arch:
                    AuxUsuario=linea.strip().split("/")
                    if AuxUsuario[0] == Usuario:
                        ValueError
                    else:
                        continue
        except IndexError:
            print("el nombre tiene que tener mas o igual a 8 caracteres")
        except ValueError:
            print("ese nombre de usuario ya esta ocupado por otra persona")
        else:
            print("el nombre es valido")
            break
    arch.close()
    return Usuario
    
def SeguridadDeContraseña():
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
                SimbolosEspeciales=["@", "!", "?", "#", "$", "¿", "¡", "&", "%", "(", ")", "=",".",",",";",":"]
                Comprobacion={"Simbolos Especiales":False,"Numeros":False,"Letras":False,"Mayusculas":False}
                for Caracter in range(len(Contraseña)):
                    aux=Contraseña[Caracter]
                    
                    if aux in SimbolosEspeciales:
                        Comprobacion["Simbolos Especiales"]=True
                    if aux.isdigit() == True:
                        Comprobacion["Numeros"]=True

                    if aux.isalpha() == True:
                        Comprobacion["Letras"]=True

                    if aux.isupper() == True:
                        Comprobacion["Mayusculas"]=True
                
                ErrorCount=0
                for Claves in Comprobacion:    
                    if Comprobacion[Claves] == False:
                        if ErrorCount==1:
                            Falta+=(f",{Claves}")
                        else:
                            Falta=(f"{Claves}")
                            ErrorCount=1
                    
                if ErrorCount == 1:
                    raise ValueError
            
            except ValueError:
                print(f"la contraseña no es suficientemente segura le faltan {Falta}")
            else:
                print("la contraseña es segura")
                break
    return Contraseña

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

