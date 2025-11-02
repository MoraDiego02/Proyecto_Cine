from AdminsSettings import MenuAdmin,MenuSuperAdmin,MenuUser
from Usuarios import EncontrarUsuario,imprimirUsuarios
from ValidacionDeDatos import validarLista
from logs import log

def MenuUser(Usuario):
    while True:
        print("1. Comprar un ticket \n 2. atencion al cliente\n 3. cerrar sesion  ")
        try:
            op=int(input("seleccione la opcion que quiere"))
            if op < 1 and op >3:
                raise ValueError
        except ValueError:
            print("ingrese Un numero que este en las opciones")
        # else:                    
        #     if op == 1:
        #         ReservaDeButacas()#hay que seleccionar la sala 
        #     if op == 2:                
        
        #     if op == 3:                
        #         break
    return


def MenuAdmin(Usuario):
    while True:
        print(" 1. revisar las solicitudes de desbloqueo \n 2. revisar el stock de la comida \n 3. Cambiar Precios Del candyBar \n 4. ver datos del Dia   \n 5. cerrar sesion  ")
        try:
            op=int(input("seleccione la opcion que quiere"))
            if op < 1 and op >5:
                raise ValueError
        except ValueError:
            print("ingrese Un numero que este en las opciones")
        # else:
        #     if op == 1:
        #         SolicitudDeDesbloqueo()
        #     if op == 2:
        #         RevisarStock()
        #     if op == 3:
        #         CambiarPreciosDelCandy()
        #     #if op == 4:
        #         #VerDatos()
        #     if op == 5:
        #         break
    

def MenuSuperAdmin(Usuario):
    while True:
        print("1. cambiar roles de usuarios \n2. cerrar sesion")
        try:
            print("seleecione la opcion que quiere:")
            op=int(input(f"{Usuario[0]}:"))
            if op < 1 and op >2:
                raise ValueError
        except ValueError:
            print("ingrese Un numero que este en las opciones")
        else:    
            if op == 1:
                CambiarRoles(Usuario)
            if op == 2:
                break
    return

def actualizarRol(rolElegido, user):
    try:
        lineasOriginales = []
        with open("cuentas.csv", "r") as archivo:
            for linea in archivo:
                lineasOriginales.append(linea)
        
        cuentasActualizadas = []
        for linea in lineasOriginales:
            partes = linea.strip().split(';')
            
            if partes[1] == user[1]:
                partes[-1] = rolElegido
                rolactualizado = ";".join(partes) + "\n"
                cuentasActualizadas.append(rolactualizado)
            else:
                cuentasActualizadas.append(linea)
                
        with open("cuentas.csv", "w") as archivo:
            for cuenta in cuentasActualizadas:
                archivo.write(cuenta)
        
        return True
    except IOError:
        print("El archivo cuentas.csv no existe")
    return False


def CambiarRoles(usuario):
    user = imprimirUsuarios(usuario)
    cuenta = EncontrarUsuario(user[0])
    if cuenta != False:
        roles = ["User","Admin","SuperAdmin"]
        print(f"Selecciono: {user[0]}")
        rolElegido = validarLista(roles)
        if actualizarRol(rolElegido,user) == True:
            print("Rol actualizado")
        else:
            print("No se pudo actualizar el rol")
    return



def CambiarPreciosDelCandy():
    
    candybar = {}
    with open("", mode="rt", encoding="utf-8") as arch:
        for linea in arch:
        # Eliminar saltos de línea y separar los datos
            datos = linea.strip().split(";")
                
                # Validar que la línea tenga todos los datos
        if len(datos) == 4:
                id_prod, producto, precio, stock, = datos
                
                    # Crear una entrada en el diccionario
                candybar[producto.title()] = {
                    "Precio": int(precio),
                    "Stock": int(stock),
                    "ID": id_prod
                    }
    return candybar

#POR IMPLEMENTAR
# def verDatos():
#     print("reservado")

# def SimularDatos():
#     print("reservado")
    
# def SolicitudDeDesbloqueo():
#     print("reservado")
    