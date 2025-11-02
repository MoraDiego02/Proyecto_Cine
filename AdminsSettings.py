from Usuarios import EncontrarUsuario,imprimirUsuarios
from ValidacionDeDatos import validarLista
from logs import log
from faker import Faker
import random
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
        print("1. cambiar roles de usuarios \n2generar cuentas\n3. cerrar sesion")
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
                generarCuentas()
            if op == 3:

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

def generarcuentas():
    fake = Faker("es_AR")

    # Pedir cuántos usuarios generar
    while True:
        try:
            cantidad = int(input("¿Cuántos usuarios querés generar?: "))
            if cantidad <= 0:
                raise ValueError
            break
        except ValueError:
            print("Por favor, ingresá un número válido mayor que 0.")

    usuarios = []

    for i in range(1, cantidad + 1):
        # Generar nombre de usuario (solo letras y números)
        nombre = fake.user_name()
        username = "".join(c for c in nombre if c.isalnum()).lower()

        # Generar DNI de 8 dígitos
        dni = str(random.randint(10_000_000, 99_999_999))

        # Generar contraseña con al menos 1 mayúscula y longitud mínima 8
        letras = "abcdefghijklmnopqrstuvwxyz"
        numeros = "0123456789"
        simbolos = "!@#$%&*?"
        mayus = random.choice(letras).upper()
        resto = "".join(random.choice(letras + letras.upper() + numeros + simbolos) for _ in range(7))
        password = mayus + resto

        # Generar fecha de nacimiento
        fecha = fake.date_of_birth(minimum_age=5, maximum_age=90)
        fecha_nac = f"{fecha.day}:{fecha.month}:{fecha.year}"

        # Crear usuario con el formato pedido
        usuario = f"{username};{password};{dni};{fecha_nac};User"
        usuarios.append(usuario)

    # Guardar en el archivo (modo append)
    with open("cuentas.csv", "a", encoding="utf-8") as f:
        for u in usuarios:
            f.write(u + "\n")

    print(f"\n✅ {cantidad} usuarios generados y guardados en 'cuentas.csv'.\n")
    return usuarios

    