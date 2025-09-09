from funciones_cine import MostrarSala
from funciones_cine import crearsala


def inicio():
    print("-" * 40)
    print("|      🎥 Bienvenido a CineUADE 🎥      |")
    print("-" * 40)
    print("-" * 40)

def main():
    print("CINEUADE")
    print("bienvenidos al cien uade")
    print("en que sucursal quiere ver la pelicula")
    print("")
    sucursal= 1 #int(input("ingrese un numero para seleccionar la sucursal"))
    print("elija un numero del 1 al 3")
    print("si quiere volver a la pagina principal ingrese -1")
    NumeroSala= 1
    while NumeroSala >= 1 or NumeroSala <= 3:
        NumeroSala=int(input("ingrese el numero de sala que quiere seleccionar "))
        while NumeroSala != -1:
            MostrarSala(crearsala(NumeroSala))
            print("que asiento quiere seleccionar para esta pelicula")
            FilaAsiento=int(input("seleccione la fila en la que quiere su asiento"))
            ColumnaAsiento=int(input("seleccione la columna en la que quiere su asiento"))
            NumeroSala= -1 # int(input("ingrese el numero de sala que quiere seleccionar -1 para salir de esto:"))


if __name__ == "__main__":
    inicio()
    main()