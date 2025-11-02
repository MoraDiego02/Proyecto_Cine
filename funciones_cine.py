import json 
import random
#import gspread
#from google.oauth2.service_account import Credentials
from Candybar import compraCandybar
from datetime import date

#precio de la entrada
def PrecioDelaEntrada(candy):
    Dias=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    GenerarDia = lambda : random.randint(0,6)
    QueDiaEs=GenerarDia()
    entrada=7500
    if 0<= QueDiaEs <= 3 :
        PrecioFinal=entrada*0.80
        print("como hoy es",Dias[QueDiaEs],"la entrada tiene un descuento del 20%!")
        print("la entrada para la pelicula esta:",PrecioFinal)
    else:
        PrecioFinal=entrada*1.10
        print("como hoy es",Dias[QueDiaEs],"la entrada tiene un aumento del 10%")
        print("la entrada para la pelicula esta:",PrecioFinal)
    print("con que quiere pagar ")
    print("ingrese 1 para pagar con tarjeta ")
    print("ingrese 2 para abonar en efectivo ")
    while True:
        try:
            MetodoDePago=int(input("ingrese el numero (1 o 2) "))
            if MetodoDePago < 1 or MetodoDePago > 2:
                raise ValueError
        except ValueError:
            print("Error, Ingrese uno de los numeros posibles")
        else:
            if MetodoDePago == 1:
                print("se selecciono tarjeta hay un 5% de recargo para este metodo de pago")
                PrecioFinal=PrecioFinal*1.05
                print("el precio final seria de:",PrecioFinal)
                break
            else: 
                print("selecciono efectivo")
                break
    PrecioFinal+=candy
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
    print("1. Para la sucursal de el Abasto")
    print("2. Para la sucursal de Palermo")
    print("3. Para la sucursal de Caballito")
    while True:
        try:
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
        

def ReservaDeButacas(Sala,info):
    Edad=info[3]
    
    Edad=calcular_edad(Edad)
    
    pelicula=EdadRating(Edad)
    
    MostrarSala(Sala)
    
    info+=pelicula
    ButacasVacias = 0
    for i in range(len(Sala)):
        for j in range(len(Sala[0])):
            if Sala[i][j] == 0:
                ButacasVacias += 1

    print("Butacas disponibles:", ButacasVacias)
    asientos=[]
    try:
        NumeroDeButacas = int(input("¿Cuántas butacas desea comprar?: "))
        if NumeroDeButacas <= 0:
            raise ValueError("Debe ingresar un número mayor que 0.")
        if NumeroDeButacas > ButacasVacias:
            raise ValueError
    except ValueError:
        print(f"No hay suficientes butacas vacías (disponibles: {ButacasVacias}).")
    else:
        asientos_reservados = []
        while NumeroDeButacas > 0:
            print("\nSeleccione la ubicación de su asiento:")
            try:
                FilaDeLaButaca = int(input("Ingrese la fila (1 a 5): ")) - 1
                if FilaDeLaButaca < 0 or FilaDeLaButaca > 4:
                    raise ValueError
            except ValueError:
                print("La fila debe estar entre 1 y 5.")
            else:
                try:
                    ColumnaDeLaButaca = int(input("Ingrese la columna (1 a 5): ")) - 1
                    if ColumnaDeLaButaca < 0 or ColumnaDeLaButaca > 4:
                        raise ValueError
                except ValueError:
                        print("La columna debe estar entre 1 y 5.")
                else:
                    if Sala[FilaDeLaButaca][ColumnaDeLaButaca] == 0:
                        Sala[FilaDeLaButaca][ColumnaDeLaButaca] = 1
                        asientos_reservados.append((FilaDeLaButaca + 1, ColumnaDeLaButaca + 1))
                        NumeroDeButacas =- 1
                        print(f"Asiento reservado correctamente: Fila {FilaDeLaButaca + 1}, Columna {ColumnaDeLaButaca + 1}")
                        asientos+=[f"F {FilaDeLaButaca+1} C {ColumnaDeLaButaca+1}"]
                    else:
                        print("Ese asiento ya está ocupado. Elija otro, por favor.")
                        print("\nResumen de asientos reservados:")
                        for fila, col in asientos_reservados:
                            print(f" - Fila {fila}, Columna {col}")
                            print()
                            print("los asientos estan reservados")

        try:
            info += asientos
            print("quiere comprar algo del candybar")
            print("1. Si 2. No ")
            opcion=int(input("ingrese el numero de la opcion que quiera: "))
            if opcion < 1 or opcion > 2:
                raise ValueError
        except ValueError:
            print("porfavor ingrese un numero de la opcion que quiere(1 o 2)")
        else:
            candycompra=0
            if opcion == 1:
                candycompra=compraCandybar(candycompra)
                    
            if opcion == 2:
                candycompra=0
            
                
    print(info[2],info[0],info[6],info[7],info[5])
    precio=PrecioDelaEntrada(candycompra)

    info.append(str(precio))
        
    comprobante(info[2],info[0],info[6],info[7],info[5],info[8],info[9])

            

def comprobante(dni,Nombre,pelicula,formato,sucursal,asiento,precio_final):#hacer tuplax
        try:
            print("1. si 2. no" )
            Opcion=int(input("ingrese el numero de la opcion que quiere"))
            if Opcion < 1 or Opcion > 2:
                ValueError
        except ValueError:
            print("Error en el ingreso")
        else:
            if Opcion == 1 :
                comprobante = (Nombre, dni, pelicula, sucursal, asiento, precio_final)
                print(f"-Nombre: {Nombre} \n-DNI: {dni} \n-Pelicula:{pelicula} formato {formato}\n-Sucursal: {sucursal} \nAsiento/s: {asiento} \n-Precio Final: {precio_final}")
                print()
            else:
                print("No se emitio comprobante.")

def simularPagos():
    random.choice
    entrada=7500    
    mult=[0.80,1.10]
    mult=random.choice(mult)
    pagosim=entrada*mult

    return pagosim




def FinDelDia(Sucursales):
    print("finalizo el dia")
    print("estos son los datos de todas la sucursales")

    Recaudaciones={
        "Abasto":0,
        "Caballito":0,
        "Palermo":0
    }

    cantasientosAbasto=0
    cantasientosCaballito=0
    cantasientosPalermo=0
    

    for i in range(len(Sucursales)):
        for j in range(len(Sucursales[i])):
            for k in range(len(Sucursales[i][j])):
                for l in range(len(Sucursales[i][j][k])):
                        if i == 0:
                            if Sucursales[i][j][k][l]==1:
                                Recaudaciones["Abasto"]+=simularPagos()
                                cantasientosAbasto+=1
                        elif i == 1:
                            if Sucursales[i][j][k][l]==1:
                                Recaudaciones["caballito"]+=simularPagos()
                                cantasientosAbasto+=1
                        else:
                            if Sucursales[i][j][k][l]==1:
                                Recaudaciones["palermo"]+=simularPagos()
                                cantasientosAbasto+=1
    Recaudaciones_total=0
    for clave in Recaudaciones:
        Recaudaciones_total+=Recaudaciones[clave]

    print(f"la recaudacion total de la sucursal Abasto es de:{Recaudaciones["Abasto"]}")
    print(f"la recaudacion total de la sucursal Caballito es de:{Recaudaciones["Caballito"]}")
    print(f"la recaudacion total de la sucursal Palermo es de:{Recaudaciones["Palermo"]}")
    print(f"la recaudacion total del dia es de:{Recaudaciones_total}")
    print("la Sucursal que mas recaudaciones: con")


    



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