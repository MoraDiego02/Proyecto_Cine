from Usuarios import EncontrarUsuario
from logs import log 


def SolicitudDeDesbloqueo():
    print("reservado")
    


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
        else:
            print("Usuario se ha encontrado")
            ArchAux=open("cuentasAux.cvs")

            try: 
                print("1.Si 2.No")
                Opcion=int(input("quiere seguir:"))
                
                if Opcion < 1 or Opcion > 2:
                    raise ValueError 
            except ValueError:
                print("ingrese un numero (1 o 2)")
            else:
                if Opcion == 1:
                    arch.close()
                    log("CambiarDeRoles",0,"SuperAdmin")
                    continue
                
                if Opcion == 2:
                    break
        return



def SimularDatos():
    print("reservado")


def CambiarPreciosDelCandy():
    
    candybar = {}

    try:
        with open("", mode="rt", encoding="utf-8") as arch:
            for linea in arch:
                # Eliminar saltos de línea y separar los datos
                datos = linea.strip().split("/")
                
                # Validar que la línea tenga todos los datos
                if len(datos) == 4:
                    producto, precio, stock, id_prod = datos
                    
                    # Crear una entrada en el diccionario
                    candybar[producto.title()] = {
                        "Precio": int(precio),
                        "Stock": int(stock),
                        "ID": id_prod
                    }
    return candybar


def verDatos():