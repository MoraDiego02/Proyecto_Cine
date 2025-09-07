import random

def crearsala(numero,sucursal,SalaCreadas):
    columnas=5
    filas=5
    if 
    if  sucursal == 1 and numero == 1:
        for i in range()
        Sala_1=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
    else:
        return sala_1
    
    if sucursal == 1 and numero == 2:
        Sala_2=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_2
    if sucursal == 1 and numero == 3:
        Sala_3=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_3

    if sucursal == 2 and numero == 1:
        Sala_4=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_4
    if sucursal == 2 and numero == 2:
        Sala_5=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_5
    if sucursal == 2 and numero == 3:
        Sala_6=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_6

    if sucursal == 3 and numero == 1:
        Sala_7=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_7
    if sucursal == 3 and numero == 2:
        Sala_8=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_8
    if  sucursal == 3 and numero == 3:
        Sala_9=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_9



def MostrarSala(matriz):
    columnas=len(matriz[1])
    print("        ",end="")
    for i in range(columnas):
        print("C" + str(i+1).ljust(6), end="  ")
    print()
    for i in range(len(matriz)):
        print("FILA",i+1,end="  ")
        for j in range(columnas):
            if matriz[i][j]<1:
                print("x".ljust(5),end="    ")
            else:
                print(" ".ljust(5),end="    ")
        print()
    return

print("bienvenidos al cien uade")
print("en que sucursal quiere ver la pelicula")
print("ingrese 1 un seleccionar")
sucursal= 1 #int(input("ingrese un numero para seleccionar la sucursal"))
print("elija un numero del 1 al 3")
print("si quiere volver a la pagina principal ingrese -1")
NumeroSala= 1
while NumeroSala >= 1 and NumeroSala <= 3:
    NumeroSala=int(input("ingrese el numero de sala que quiere seleccionar "))
    while NumeroSala != -1:
        MostrarSala(crearsala(NumeroSala))
        print("que asiento quiere seleccionar para esta pelicula")
        FilaAsiento=int(input("seleccione la fila en la que quiere su asiento"))
        ColumnaAsiento=int(input("seleccione la columna en la que quiere su asiento"))
        NumeroSala= -1 # int(input("ingrese el numero de sala que quiere seleccionar -1 para salir de esto:"))

def nosecomoponer(): 
    if sucursal == 1 and NumeroSala == 1:
        BuscarAsiento(crearsala(NumeroSala))
    if sucursal == 1 and NumeroSala == 2:
        BuscarAsiento(crearsala(NumeroSala))
    if sucursal == 1 and NumeroSala == 3:
        BuscarAsiento(crearsala(NumeroSala))

    if sucursal == 1 and NumeroSala == 1:
        BuscarAsiento(crearsala(NumeroSala))
    if sucursal == 1 and NumeroSala == 2:
        BuscarAsiento(crearsala(NumeroSala))
    if sucursal == 1 and NumeroSala == 3:
        BuscarAsiento(crearsala(NumeroSala))

    if sucursal == 1 and NumeroSala == 1:
        BuscarAsiento(crearsala(NumeroSala))
    if sucursal == 1 and NumeroSala == 2:
        BuscarAsiento(crearsala(NumeroSala))
    if sucursal == 1 and NumeroSala == 3:
        BuscarAsiento(crearsala(NumeroSala))


"""
def PagarLosAsiento():
    for i in range():
    if 
    print("el asiento esta disponible")



def reportardinerodiario():
    Preciopelicula=7.084,93"""



if __name__ == "__main__":
    CrearSala()



