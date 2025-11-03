
import random
import gspread
from google.oauth2.service_account import Credentials
from Candybar import compraCandybar
from datetime import date
from logs import log

def PrecioDelaEntrada(candy):
    import random

    Dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    QueDiaEs = random.randint(0, 6)

    entrada = 7500.0
    if 0 <= QueDiaEs <= 3:
        PrecioFinal = entrada * 0.80
        print(f"Como hoy es {Dias[QueDiaEs]} la entrada tiene un descuento del 20%!")
    else:
        PrecioFinal = entrada * 1.10
        print(f"Como hoy es {Dias[QueDiaEs]} la entrada tiene un aumento del 10%")
    print()
    print("La entrada para la película está:", PrecioFinal)
    print()
    print("¿Con qué quiere pagar?")
    print()
    print("Ingrese 1 para pagar con tarjeta")
    print()
    print("Ingrese 2 para abonar en efectivo")

    while True:
        try:
            MetodoDePago = int(input("Ingrese el número (1 o 2): "))
            if MetodoDePago not in (1, 2):
                raise ValueError
            break
        except ValueError:
            print("Error, ingrese 1 o 2.")

    if MetodoDePago == 1:
        print()
        print("Se seleccionó tarjeta: hay un 5% de recargo.")
        PrecioFinal *= 1.05
        print("El precio final (solo entradas) sería de:", PrecioFinal)
    else:
        print("Seleccionó efectivo.")

    try:
        candy_num = float(candy)
    except (TypeError, ValueError):
        candy_num = 0.0

    PrecioFinal += candy_num
    return PrecioFinal

def MostrarSala(matriz):
    columnas=len(matriz[0])
    print("        ",end="")
    for i in range(columnas):
        print("C" + str(i+1).ljust(6), end="  ")
    print()
    for i in range(len(matriz)):
        print("FILA",i+1,end="  ")
        for j in range(columnas):
            if matriz[i][j] == 1:
                print("x".ljust(5),end="    ")
            else:
                print(" ".ljust(5),end="    ")
        print()
    return matriz

def CargarSucursales():

    filas=5
    columnas=5
    SucursalAbasto=[[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]for i in range(3)]
    SucursalCaballito=[[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]for i in range(3)]
    SucursalPalermo=[[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]for i in range(3)]
    sucursal=[SucursalAbasto,SucursalCaballito,SucursalPalermo]
    return sucursal


def SeleccionarSucursal(Sucursal,info):
    
    NombresDeSucursal=["Sucursal Abasto","Sucursal Caballito","Sucursal Palermo",]
    SucursalAbasto = Sucursal[0]
    SucursalCaballito = Sucursal[1]
    SucursalPalermo = Sucursal[2]
    print()
    print("1. Para la sucursal de el Abasto")
    print("2. Para la sucursal de Palermo")
    print("3. Para la sucursal de Caballito")
    while True:
        try:
            print()
            NumeroDeSucursal = int(input("Ingrese el número de sucursal (1 a 3): ")) - 1
            if NumeroDeSucursal < 0 or NumeroDeSucursal > 2:
                raise ValueError
        except ValueError:
           print("El número de sucursal debe estar entre 1 y 3.")
        else:
            try:
                NumeroDeSala = int(input("Ingrese el número de sala (1 a 3): ")) - 1
                if NumeroDeSala < 0 or NumeroDeSala > 2:
                    raise ValueError
            except ValueError:
                print("El número de sala debe estar entre 1 y 3.")
            else:
                if NumeroDeSucursal == 0:
                    sala_matriz = SucursalAbasto[NumeroDeSala]
                elif NumeroDeSucursal == 1:
                    sala_matriz = SucursalPalermo[NumeroDeSala]
                elif NumeroDeSucursal == 2:
                    sala_matriz = SucursalCaballito[NumeroDeSala]
                break
    
    info+=[f"{NombresDeSucursal[NumeroDeSucursal]} - Sala {NumeroDeSala + 1}"]
    
    ReservaDeButacas(sala_matriz,info)
        
def ReservaDeButacas(Sala, info):
    Edad = calcular_edad(info[3])
    pelicula = EdadRating(Edad)
    MostrarSala(Sala)
    info += pelicula

    ButacasVacias = sum(1 for i in range(len(Sala)) for j in range(len(Sala[0])) if Sala[i][j] == 0)
    print("Butacas disponibles:", ButacasVacias)

    asientos = []
    asientos_reservados = []

    try:
        print()
        NumeroDeButacas = int(input("¿Cuántas butacas desea comprar?: "))
        if NumeroDeButacas <= 0 or NumeroDeButacas > ButacasVacias:
            raise ValueError
    except ValueError:
        print(f"No hay suficientes butacas vacías (disponibles: {ButacasVacias}).")
        return
    else:
        while NumeroDeButacas > 0:
            print()
            print("\nSeleccione la ubicación de su asiento:")

            try:
                print()
                f = int(input("Ingrese la fila (1 a 5): ")) - 1
                if f < 0 or f > 4:
                    raise ValueError
            except ValueError:
                print("La fila debe estar entre 1 y 5.")
                continue

            try:
                print()
                c = int(input("Ingrese la columna (1 a 5): ")) - 1
                if c < 0 or c > 4:
                    raise ValueError
            except ValueError:
                print("La columna debe estar entre 1 y 5.")
                continue

            if Sala[f][c] == 0:
                Sala[f][c] = 1
                asientos_reservados.append((f + 1, c + 1))
                asientos.append(f"F {f + 1} C {c + 1}")
                NumeroDeButacas -= 1
                print(f"Asiento reservado: Fila {f + 1}, Columna {c + 1}")
            else:
                print("Ese asiento ya está ocupado. Elija otro, por favor.")

    if asientos_reservados:
        print("\nResumen de asientos reservados:")
        for fila, col in asientos_reservados:
            print(f" - Fila {fila}, Columna {col}")
        print("\nLos asientos están reservados.")

    info += asientos

    candy_total = 0.0
    print()
    print("¿Quiere comprar algo del candybar?")
    while True:
        try:
            print("1. Sí   2. No")
            opcion = int(input("Ingrese el número de la opción que quiera: "))
            if opcion not in (1, 2):
                raise ValueError
            break
        except ValueError:
            print("Por favor ingrese 1 o 2.")

    if opcion == 1:
        candy_total = float(compraCandybar())

    precio = PrecioDelaEntrada(candy_total)
    info.append(str(precio))

    comprobante(info[0], info[2], info[6], info[5], info[7], asientos, precio)

def comprobante(dni,Nombre,pelicula,formato,sucursal,asiento,precio_final):
        try:
            print("Desea su comprobante? 1. si 2. no: " )
            Opcion=int(input("ingrese el numero de la opcion que quiere"))
            if Opcion < 1 or Opcion > 2:
                ValueError
        except ValueError:
            print("Error en el ingreso")
        else:
            if Opcion == 1 :
                print()
                comprobante = (Nombre, dni, pelicula, sucursal, asiento, precio_final)
                print(f"-Nombre: {Nombre} \n-DNI: {dni} \n-Pelicula:{pelicula} formato {formato}\n-Sucursal: {sucursal} \nAsiento/s: {asiento} \n-Precio Final: {precio_final}")
                print()
            else:
                print("No se emitio comprobante.")

import random
from datetime import datetime

def simularPagos():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    hoy = datetime.now().weekday()
    entrada = 7500
    if hoy <= 3:
        precio = entrada * 0.8
    else:
        precio = entrada * 1.1

    metodo = random.choice(["tarjeta", "efectivo"])
    if metodo == "tarjeta":
        precio *= 1.05
    return precio

def FinDelDia(Sucursales,Usuario):
    Recaudaciones = {"Abasto": 0, "Caballito": 0, "Palermo": 0}
    Butacas = {"Abasto": 0, "Caballito": 0, "Palermo": 0}
    log("FinDelDia",1,Usuario)

    for i in range(len(Sucursales)):
        for j in range(len(Sucursales[i])):
            for k in range(len(Sucursales[i][j])):
                for l in range(len(Sucursales[i][j][k])):
                    if Sucursales[i][j][k][l] == 1:
                        if i == 0:
                            Recaudaciones["Abasto"] += simularPagos()
                            Butacas["Abasto"] += 1
                        elif i == 1:
                            Recaudaciones["Caballito"] += simularPagos()
                            Butacas["Caballito"] += 1
                        else:
                            Recaudaciones["Palermo"] += simularPagos()
                            Butacas["Palermo"] += 1

    total = sum(Recaudaciones.values())
    mayor_sucursal = max(Recaudaciones, key=Recaudaciones.get)

    with open("recuentodebutacas.csv", "a") as f:
        for suc in Butacas:
            f.write(f"{suc},{Butacas[suc]}\n")

    with open("recaudacion_por_sucursal.csv", "a") as f:
        for suc in Recaudaciones:
            f.write(f"{suc},{Recaudaciones[suc]:.2f}\n")

    with open("recaudacion_total.csv", "a") as f:
        f.write(f"Total,{total:.2f}\n")

    with open("mayor_recaudacion.csv", "a") as f:
        f.write(f"{mayor_sucursal},{Recaudaciones[mayor_sucursal]:.2f}\n")

    print("Recuento de butacas ocupadas:")
    for suc, cant in Butacas.items():
        print(f"{suc}: {cant}")
    print("\nRecaudación por sucursal:")
    for suc, rec in Recaudaciones.items():
        print(f"{suc}: ${rec:.2f}")
    print(f"\nRecaudación total del día: ${total:.2f}")
    print(f"Sucursal con mayor recaudación: {mayor_sucursal} (${Recaudaciones[mayor_sucursal]:.2f})")
    



def calcular_edad(info):

    info=str(info)
    info=info.strip().split(":")
    anio=int(info[2])
    mes=int(info[1])
    dia=int(info[0])
    hoy = date.today()
    nacimiento = date(anio, mes, dia)
    edad = hoy.year - nacimiento.year

    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        edad -= 1

    return edad

                                    
def EdadRating(Edad):
    peliculas = {
        "ATP": {
            "descripcion": "Apta para todo público.",
            "titulos": ["Toy Story", "Coco", "Buscando a Nemo", "Kung Fu Panda"]
        },
        "+13": {
            "descripcion": "Puede contener violencia leve o temas más maduros.",
            "titulos": ["Los Vengadores", "Jurassic World", "Spider-Man", "Piratas del Caribe"]
        },
        "+16": {
            "descripcion": "Contiene violencia intensa o lenguaje fuerte.",
            "titulos": ["Inception", "El Caballero Oscuro", "John Wick", "Matrix"]
        },
        "+18": {
            "descripcion": "Solo para adultos. Puede incluir violencia o contenido explícito.",
            "titulos": ["El Padrino", "Scarface", "Pulp Fiction", "El Lobo de Wall Street"]
        }
    }

    if Edad < 13:
        categoria = "ATP"
    elif Edad < 16:
        categoria = "+13"
    elif Edad < 18:
        categoria = "+16"
    else:
        categoria = "+18"

    print(f"\nClasificación: {categoria}")
    print(f"Descripción: {peliculas[categoria]['descripcion']}")
    print("\nPelículas disponibles:")

    contador = 1
    for titulo in peliculas[categoria]["titulos"]:
        print(f"{contador}. {titulo}")
        contador += 1

    while True:
        try:
            opcion = int(input("\nElige el número de la película: ")) - 1
            if opcion < 0 or opcion >= len(peliculas[categoria]["titulos"]):
                raise ValueError
            break
        except ValueError:
            print("Opción inválida. Intenta nuevamente.")

    pelicula_elegida = peliculas[categoria]["titulos"][opcion]

    formatos = ["2D", "3D"]
    print("\nFormatos disponibles:")
    contador = 1
    for f in formatos:
        print(f"{contador}. {f}")
        contador += 1

    while True:
        try:
            opcion_formato = int(input("\nElige el formato: ")) - 1
            if opcion_formato not in (0, 1):
                raise ValueError
            break
        except ValueError:
            print("Formato inválido. Elige 1 o 2.")

    formato_elegido = formatos[opcion_formato]

    return pelicula_elegida,formato_elegido

            

"""
def spreadsheet():

  scopes = [
      "https://www.googleapis.com/auth/spreadsheets",
      "https://www.googleapis.com/auth/drive"
  ]

  cred = Credentials.from_service_account_file("cineuade-1ca1650b48f9.json", scopes=scopes)
  gc = gspread.authorize(cred)
  sh = gc.open("CineUade")
  print(sh.sheet1.acell("A1").value)

  spreadsheet_name = "CineUade"
  worksheet_name = "Sheet1"

  spreadsheet = gc.open(spreadsheet_name)
  worksheet = spreadsheet.worksheet(worksheet_name)

  worksheet.clear()
  with open("Example.csv", 'r', encoding='utf-8') as file:
      for i, linea in enumerate(file, start=1):
          aux = linea.strip().split(",")  # separa por comas y elimina \n
          worksheet.insert_row(aux, index=i)
spreadsheet()"""