from ActualizacionDeArchivos import reinicioDeContraseña,EncontrarUsuario
from logs import log
def CrearCuenta():#este es para exportar la cuenta creada a el archivo
    arch=open("cuentas.cvs",mode="at")
    Usuario=NombreDeusuario()
    Contraseña=SeguridadDeContraseña()
    Documento=ComprobacionDeDniYFecha(1)
    Fecha=ComprobacionDeDniYFecha(2)
    Datos=(f"{Usuario}/{Contraseña}/{Documento}/{Fecha}/User\n")
    
    arch.write(Datos)
    arch.close
    
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

def EnviarMensajeAAC(Opcion):

    with open("Mensajes/Solicitudes.cvs",mode="at") as Arch:

        print("bienvenido a atencion al cliente")
        print("ingrese el tipo de mensaje que quiere enviar")
        while Opcion!=2:
            print("1.segurencia 2.Solicitud De reinicio de contraseña ")
    
            MENS=int()
            Mensaje=print("ingrese el mensajes:")

            print("desea mandar otro mensaje")
            print("1. enviar otro mensaje 2. para salir ")
            Opcion=int(input("ingrese su seleccion: "))

        return Opcion
    

def reinicioDeContraseña():
    print("para poder autentificar que la cuenta es suya vamos a pedir los siguientes datos")
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
        
    UsuarioNom=Cuenta[0]
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
    arch.close()

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

    print("Contraseña actualizada correctamente.")
        
    log("reiniciodecontraseña",3,UsuarioNom)
    return 
