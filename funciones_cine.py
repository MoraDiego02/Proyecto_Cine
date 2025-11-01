import json 
import random
#precio de la entrada
def PrecioDelaEntrada():
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
        except ValueError:
            print("Error, Ingrese uno de los numeros posibles")
            continue
        else:
            break

    if MetodoDePago == 1:
        print("se selecciono tarjeta hay un 5% de recargo para este metodo de pago")
        PrecioFinal=PrecioFinal*1.05
        print("el precio final seria de:",PrecioFinal)
        return PrecioFinal
    else: 
        print("selecciono efectivo")
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


def SeleccionarSucursal(Sucursal):
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
                raise ValueError("El número de sucursal debe estar entre 1 y 3.")

            NumeroDeSala = int(input("Ingrese el número de sala (1 a 3): ")) - 1
            if NumeroDeSala < 0 or NumeroDeSala > 2:
                raise ValueError("El número de sala debe estar entre 1 y 3.")

            break  # Si todo salió bien, sale del bucle

        except ValueError as e:
            print("Error:", e)
            print("Por favor, ingrese valores válidos.\n")


    if NumeroDeSucursal == 0:
        sala_matriz = SucursalAbasto[NumeroDeSala]
    elif NumeroDeSucursal == 1:
        sala_matriz = SucursalPalermo[NumeroDeSala]
    elif NumeroDeSucursal == 2:
        sala_matriz = SucursalCaballito[NumeroDeSala]

    ReservaDeButacas(MostrarSala(sala_matriz))
    return NumeroDeSucursal, NumeroDeSala


def ReservaDeButacas(Sala):
    ButacasVacias = 0
    for i in range(len(Sala)):
        for j in range(len(Sala[0])):
            if Sala[i][j] == 0:
                ButacasVacias += 1

    print("Butacas disponibles:", ButacasVacias)
    print()

    
    while True:
        try:
            NumeroDeButacas = int(input("¿Cuántas butacas desea comprar?: "))
            if NumeroDeButacas <= 0:
                raise ValueError("Debe ingresar un número mayor que 0.")
            if NumeroDeButacas > ButacasVacias:
                raise ValueError(f"No hay suficientes butacas vacías (disponibles: {ButacasVacias}).")
            break
        except ValueError as e:
            print("Error:", e)

    asientos_reservados = []

    
    while NumeroDeButacas > 0:
        print("\nSeleccione la ubicación de su asiento:")

        
        while True:
            try:
                FilaDeLaButaca = int(input("Ingrese la fila (1 a 5): ")) - 1
                if FilaDeLaButaca < 0 or FilaDeLaButaca > 4:
                    raise ValueError("La fila debe estar entre 1 y 5.")
                break
            except ValueError as e:
                print("Error:", e)

        
        while True:
            try:
                ColumnaDeLaButaca = int(input("Ingrese la columna (1 a 5): ")) - 1
                if ColumnaDeLaButaca < 0 or ColumnaDeLaButaca > 4:
                    raise ValueError("La columna debe estar entre 1 y 5.")
                break
            except ValueError as e:
                print("Error:", e)

        
        if Sala[FilaDeLaButaca][ColumnaDeLaButaca] == 0:
            Sala[FilaDeLaButaca][ColumnaDeLaButaca] = 1
            asientos_reservados.append((FilaDeLaButaca + 1, ColumnaDeLaButaca + 1))
            NumeroDeButacas -= 1
            print(f"Asiento reservado correctamente: Fila {FilaDeLaButaca + 1}, Columna {ColumnaDeLaButaca + 1}")
        else:
            print("Ese asiento ya está ocupado. Elija otro, por favor.")

    
    print("\nResumen de asientos reservados:")
    for fila, col in asientos_reservados:
        print(f" - Fila {fila}, Columna {col}")
    print()

 


def comprobante(dni,pelicula,sucursal,sala,asiento,precio_final,Nombre):#hacer tuplax
    print("Comprobante de pago")
    print("Nombre", Nombre)
    print("DNI:", dni)
    print("Pelicula:", pelicula)
    print("Sucursal:", sucursal)
    print("Sala:", sala)
    print("Asiento:", asiento)
    print("Precio final:", precio_final)
    print("¡Gracias por su compra!")


def formato():
    print("2D")
    print("3D")
    print("4D")
    while True:
        try:
            formato = int(input("Seleccione el formato de la película (1-3): "))
            while formato < 1 or formato > 3:
                formato = int(input("Incorrecto, Seleccione un formato válido (1-3): "))
            break
        except ValueError:
            print("Error")
            continue
    if formato == 1:
        return "2D"
    elif formato == 2:
        return "3D"
    else:
        return "4D"

def FinDelDia(Sucursales):
    recaudaciones_totales= []
    SCaballito=0
    SPalermo=0
    SAbasto=0

    print("finalizo el dia")
    print("estos son los datos de todas la sucursales")

    for i in range(len(Sucursales)):
        for j in range(len(Sucursales[i])):
            for k in range(len(Sucursales[i][j])):
                for l in range(len(Sucursales[i][j][k])):
                        if i == 0:
                            if Sucursales[i][j][k][l]==1:
                                SAbasto+=7500
                        elif i == 1:
                            if Sucursales[i][j][k][l]==1:
                                SCaballito+=7500
                        else:
                            if Sucursales[i][j][k][l]==1:
                                SPalermo+=7500
    recaudaciones_totales.append(SAbasto)
    recaudaciones_totales.append(SCaballito)
    recaudaciones_totales.append(SPalermo)
    print("la recaudacion total de la sucursal Abasto es de:",recaudaciones_totales[0])
    print("la recaudacion total de la sucursal Caballito es de:",recaudaciones_totales[1])
    print("la recaudacion total de la sucursal Palermo es de:",recaudaciones_totales[2])
    print("la recaudacion total del dia es de:",sum(recaudaciones_totales))


def FinalDelDia():
    print("hola es el final del dia") 

def agecheck():
    while True:
        m30=[4,6,9,11]
        try:
            dia=int(input("Ingrese el dia que cumple años (sin mes):"))
            if dia<1 or dia>31:
                print("Error, Ingrese un dia valido")
                continue

            mes=int(input("Ingrese su mes de cumpleaños(formato numerico):"))
            if mes<1 or mes>12:
                if mes in m30 and dia==31:
                    print("Error, Ingrese el dia o mes correecto")
                    continue
                elif mes==2 and dia>=29:
                    print("Error, Ingrese el dia o mes correecto")
                    continue
                print("Error, ingrese un mes vratingalido")
                continue
                        
            año=int(input("Ingrese el año que nació:"))
            if año<1920 or año>2025:
                print("Error, ingrese un año valido")
                continue
            break
        except ValueError:
            print("Error, Ingrese un numero")
            continue

    req=0   
    if año == 2007:
        if mes==11:
            if dia<=2:
                req=18
            else:
                req=13
        elif mes>11:
            req=13
        else:
            req=18

    elif año >2007:
        if año==2012:
            if mes==11:
                if dia<=2:
                    req=13
                else:
                    req=0
            elif mes>11:
                req=0
            else:
                req=13
        elif año>2012:
            req=0
        else:
            req=13
    else:
        req=18
    return req



def EdadRating():
    
    with open("jtest.json", "r") as file :
        rating=json.load(file)
        codigos={}
        codsave=0
        peliculas = ["Avatar: El camino del agua","El gato con botas 2","John Wick 4","Super Mario","Chainsaw Man","Cretaceous Establishment","Superman","Interestelar","Fullmetal Alchemist","City of Tears","Cars","Forest Gump","Viernes 13","Angry Birds","Crimen y Castigo"]
        for i in range (len(peliculas)):
            low=peliculas[i].lower()
            codigos[low]=codsave
            codsave=codsave+1
        codigos["-1"]=999

        atp=[]
        pg=[]
        ad=[]
        used=[]
    
        while len(ad)<4:
            rand=random.randint(0,len(codigos)-2)
            if rand in used:
                rand=999
            else:
              used.append(rand)   

            aux=str(rand)
            if rating[aux]<=0:
                atp.append(peliculas[rand])
            if rating[aux]<=13:
                pg.append(peliculas[rand])
            if rating[aux]<=18:
                ad.append(peliculas[rand])
        
        age=agecheck()
                                
        if age >=18:
            print("Las peliculas disponibles son:",ad)
        elif age >=13:
            print("Las peliculas disponibles para adolecentes son:",pg)
        else:
             print("Las peliculas disponibles para infantes",atp)
            

def SimularDatos():
    print("espacio reservado")