import random
def peliculas():
    print("Listado de peliculas: ")
    print("1. Avatar: El camino del agua")
    print("2. El gato con botas 2")
    print("3. Super Mario Bros")
    print("4. Barbie")
    print("5. M3GAN")
    print("6. La ballena")
    print("7. Oppenheimer")
    print("8. Indiana Jones y el dial del destino")
    print("9. Transformers: El despertar de las bestias")
    print("10. Guardianes de la galaxia Vol. 3")
    
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

def busq_mat(matrix,target): #buscar en matriz
    total_fila=len(matrix)
    total_columnas=len(matrix[0])
    mini,maxi=0,(total_columnas*total_fila)-1
    while mini<=maxi:
        mid= (mini+maxi)//2
        fila=mid//total_fila
        col=mid%total_columnas

        if matrix[fila][col] == target:
            return True

        
        elif matrix[fila][col] < target:
            mini= mid+1

        else:
            maxi= mid-1
    return False


def crearsala(filas,columnas,numero ):
    if numero == 1:
        Sala_1=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_1
    if numero == 2:
        Sala_2=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_2
    if numero == 3:
        Sala_3=[[random.randint(0,1)for i in range(columnas)]for i in range(filas)]
        return Sala_3
    
