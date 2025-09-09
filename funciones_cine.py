import random

#precio de la entrada
def PrecioDelaEntrada():
    Dias=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    QueDiaEs=random.randint(0,6)
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
    MetodoDePago=int(input("ingrese el numero (1 o 2) "))
    while 1 != MetodoDePago != 2:
        MetodoDePago=int(input("porfavor ingrese un numero del 1 al 2 "))
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
    SucursalAbasto=Sucursal[0]
    SucursalCaballito=Sucursal[1]
    SucursalPalermo=Sucursal[2]
    print("1. Para la sucursal de el Abasto")
    print("2. Para la sucursal de Palermo")
    print("3. Para la sucursal de Caballito")
    NumeroDeSucursal=int(input("ingrese el numero de la sucursal desea seleccionar: "))-1
    while 3 <= NumeroDeSucursal <=1:
        NumeroDeSucursal=int(input("ingrese el numero de sala que desea seleccionar: "))-1

    NumeroDeSala=int(input("ingrese el numero de sala que desea seleccionar (1 a 3) "))-1
    while 3 <= NumeroDeSala <=1:
        NumeroDeSala=int(input("ingrese el numero de sala que desea seleccionar (1 a 3) "))-1

    if NumeroDeSucursal == 0:
        for i in range(len(SucursalAbasto[0])):
            if NumeroDeSala == i:
                ReservaDeButacas(MostrarSala(SucursalCaballito[0][i]))

    if NumeroDeSucursal == 1:
        for i in range(len(SucursalPalermo[0])):
            if NumeroDeSala == i:
                ReservaDeButacas(MostrarSala(SucursalCaballito[0][i]))

    if NumeroDeSucursal == 2:
        for i in range(len(SucursalCaballito[0])):
            if NumeroDeSala == i:
                ReservaDeButacas(MostrarSala(SucursalCaballito[0][i]))


def ReservaDeButacas(Sala):
    ButacasVacias=0
    for i in range(len(Sala)):
        for j in range(len(Sala[0])):
            if Sala[i][j] == 0:
                ButacasVacias+=1

    NumeroDeButacas=int(input("ingrese el numero de la cantidad de butacas que quiere comprar: "))
    while NumeroDeButacas > ButacasVacias or NumeroDeButacas <= 0:
        if NumeroDeButacas <= 0:
            print("ingrese un numero mayor que",NumeroDeButacas,"porfavor")
            NumeroDeButacas=int(input("ingrese el numero de la cantidad de butacas que quiere comprar: "))
        else:
            print("no hay suficientes butacas vacias")
            print("la cantidad de butacas vacias es:",ButacasVacias,"porfavor ingrese un numero menor o igual a que este")
            NumeroDeButacas=int(input("ingrese el numero de la cantidad de butacas que quiere comprar: "))
    while NumeroDeButacas>=1:
        FilaDeLaButaca=0
        ColumnaDeLaButaca=0
        print("a continuacion seleccione la fila en la que quiere su asiento")
        FilaDeLaButaca=int(input("ingrese un numero del 1 al 5 "))-1
        print("ahora seleccione en que lugar de la columna le gustaria sentarse")
        ColumnaDeLaButaca=int(input("ingrese un numero del 1 al 5 "))-1
        while ColumnaDeLaButaca>5 or ColumnaDeLaButaca < 0:
            print("pedilo")

        print(FilaDeLaButaca)
        print(Sala)
        for i in range(len(Sala)):
            for j in range(len(Sala[0])):
                if i == FilaDeLaButaca and j == ColumnaDeLaButaca:
                    if Sala[i][j] == 0:
                        print("el asiento esta libre ")
                        print("ya lo reservamos para usted")
                        Sala[i][j]== 1
                        NumeroDeButacas=+-1
                    else:
                        print("el asiento esta ocupado porfavor eliga otro")                
    return FilaDeLaButaca,ColumnaDeLaButaca


def comprobante(dni,pelicula,sucursal,sala,asiento,precio_final,Nombre):
    print("Comprobante de pago")
    print("Nombre", Nombre)
    print("DNI:", dni)
    print("Pelicula:", pelicula)
    print("Sucursal:", sucursal)
    print("Sala:", sala)
    print("Asiento:", asiento)
    print("Precio final:", precio_final)
    print("¡Gracias por su compra!")

def cartelera():
    peliculas = [
        "Cartelera de Películas:",
        "1. Avatar: El camino del agua",
        "2. El gato con botas 2",
        "3. John Wick 4",
        "4. Super Mario"
    ]
    for peli in peliculas:
        print(peli)

def formato():
    print("2D")
    print("3D")
    print("4D")
    formato = int(input("Seleccione el formato de la película (1-3): "))
    while formato < 1 or formato > 3:
        formato = int(input("Por favor, seleccione un formato válido (1-3): "))
    if formato == 1:
        return "2D"
    elif formato == 2:
        return "3D"
    else:
        return "4D"

     

def FinDelDia():
    filas=5
    columnas=5
    SucursalAbasto=[[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]for i in range(3)]
        
    SucursalCaballito=[[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]for i in range(3)]
        
    SucursalPalermo=[[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]for i in range(3)]
        
    Sucursales=(SucursalAbasto,SucursalCaballito,SucursalPalermo)


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

    print("plata conseguida en el dia en la sucursal abasto:",SAbasto)
    print("plata conseguida en el dia en la sucursal Caballito:",SCaballito)
    print("plata conseguida en el dia en la sucursal Palermo:",SPalermo)
