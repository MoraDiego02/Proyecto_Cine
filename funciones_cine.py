import random

#precio de la entrada
def PrecioDelaEntrada():
    Dias=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    QueDiaEs=random.randint(0,6)
    print(Dias[QueDiaEs])
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
    print("ingrese 2 para abonar con efectivo ")
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

#def DatosDelCliente(preciofinal):
"""
horas=['15:30','17:30','19:30']


def ComprobanteDePago(ButacasReservadas,Preciofinal,DatosDelclientes):
"""
####faltan comprobante de pago y lo del dni 

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
    SucursalAbasto=[[[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]for i in range(3)]]
    SucursalCaballito=[[[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]for i in range(3)]]
    SucursalPalermo=[[[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]for i in range(3)]]
    return SucursalAbasto,SucursalCaballito,SucursalPalermo


def SeleccionarSucursal(SucursalAbasto,SucursalCaballito,SucursalPalermo):
    print("1. Para la sucursal de el Abasto")
    print("2. Para la sucursal de Palermo")
    print("3. Para la sucursal de Caballito")
    NumeroDeSucursal=int(input("ingrese el numero de la sucursal desea seleccionar: "))-1
    while 3 <= NumeroDeSucursal <=1:
        NumeroDeSucursal=int(input("ingrese el numero de sala que desea seleccionar: "))-1

    NumeroDeSala=1-1#int(input("ingrese el numero de sala que desea seleccionar (1 a 3) "))-1

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


def ReservaDeButacas(sala):
    NumeroDeAsientos=int(input("ingrese el numero de asientos que quiere comprar: "))
    print(sala.count(0))
    ColumnaButaca=0
    FilaButaca=0


def BuscarAsiento(fila,columna,sala):
    if 0 <= fila == len(sala) and 0 <= columna == len(sala[0]):
        return True
    else:
        return False

def comprobante(dni,pelicula,sucursal,sala,asiento,precio_final):
    print("Comprobante de pago")
    print("DNI:", dni)
    print("Pelicula:", pelicula)
    print("Sucursal:", sucursal)
    print("Sala:", sala)
    print("Asiento:", asiento)
    print("Precio final:", precio_final)
    print("¡Gracias por su compra!")

def cartelera():
    peliculas = [
        "1. Avatar: El camino del agua",
        "2. El gato con botas 2",
        "3. John Wick 4",
        "4. Super Mario"
    ]
    for peli in peliculas:
        print(peli)
     





