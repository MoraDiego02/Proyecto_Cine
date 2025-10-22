def CrearCuenta():#este es para exportar la cuenta creada a el archivo
    arch=open("cuentas.cvs"mode=at)
    Usuario=NombreDeusuario()
    Contraseña=SeguridadDeContraseña()
    Documento=ComprobacionDeDniYFecha()
    Fecha=ComprobacionDeDniYFecha()
    Datos=(Usuario+"_"+Contraseña+"_"+Documento+"_"+Fecha+)
    RegistroDeUsuario(1)

    arch.write(Datos)

def IniciarSesion():#esta es para verificar 
    while True:

        try:
            Usuario=input("ingrese su nombre de usuario")
            if VerificacionDeDatos(1,Usuario)== False:
                raise ValueError
        except ValueError:
            print("el nombre de usuario que ingreso no es valido")
        finally:
            print("el usuario es valido")

        try:
            contraseña=input("ingrese la contraseña")
            if VerificacionDeDatos(2,contraseña)== False:
                raise ValueError
        except ValueError:
            print("la contraseña no es valida")
        finally:
            print("se a realizado el logueo de la cuenta con exito!")
            break


def RegistroDeUsuario(Opcion):
    if Opcion == 1:
       Usuario=IniciarSesion() 
                
    else:#este es el que crear las cuentas
        CrearCuenta()
            
    return Usuario
    
def VerificacionDeDatos(OP,Dato):#este va con el de Inicio de sesion
    if OP==1:
        print("")
    else:
        
        
        

def reinicioDeContraseña(Usuario):#este lo voy a mandar a usuario si pone mas de 3 veces la contraseña
    while True:

        
        break

def SeguridadDeContraseña(contraseña):#este va a ser el creador de contraseña
    while True:

        break
def NombreDeusuario(Usuario):#este es para verificar de que el nombre de usuario este disponible
    arch=open("cuentas.cvs",mode="rt")
    while True:
        print("el nombre de usuario tiene que tener mas de 8 caracteres")
        try:
            Usuario=input("nombre de usuario:")
            if len(Usuario)<8:
                raise ValueError
            else:
                while AuxUsuario:
                    AuxUsuario=arch.readline()
                    if AuxUsuario == Usuario:
                        ValueError
                    else:
                        continue
                break

        except ValueError:
            print("el nombre tiene que tener mas o - caracteres ")
        finally:
            print("el nombre es valido")
            break
    arch.close()

def ComprobacionDeDniYFecha(Opcion):
    if Opcion == 1:
        while True:
            try:
                documento=int(input("ingrese su DNI sin puntos:"))
                if documento <10000000 or documento >99999999:
                    raise ValueError
                break
            except ValueError:
                print("el DNI ingresado no es valido")
            finally:
                print("el DNI es valido")
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
                break
            except ValueError:
                print("La fecha de nacimiento es invalida. Volve a intentarlo")
            finally:
                print("La fecha de nacimiento es valida")
        return str (fecha)

