from Usuarios import EncontrarUsuario,imprimirUsuarios
from ValidacionDeDatos import validarLista
from logs import log
from faker import Faker
import random

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
    log()
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
       
        nombre = fake.user_name()
        username = "".join(c for c in nombre if c.isalnum()).lower()

      
        dni = str(random.randint(10_000_000, 99_999_999))

       
        letras = "abcdefghijklmnopqrstuvwxyz"
        numeros = "0123456789"
        simbolos = "!@#$%&*?"
        mayus = random.choice(letras).upper()
        resto = "".join(random.choice(letras + letras.upper() + numeros + simbolos) for _ in range(7))
        password = mayus + resto

       
        fecha = fake.date_of_birth(minimum_age=5, maximum_age=90)
        fecha_nac = f"{fecha.day}:{fecha.month}:{fecha.year}"

        
        usuario = f"{username};{password};{dni};{fecha_nac};User"
        usuarios.append(usuario)

    with open("cuentas.csv", "a", encoding="utf-8") as f:
        for u in usuarios:
            f.write(u + "\n")

    print(f"\n✅ {cantidad} usuarios generados y guardados en 'cuentas.csv'.\n")
    return usuarios

def revisarstock():
    