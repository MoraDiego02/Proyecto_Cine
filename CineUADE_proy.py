from funciones_cine import MostrarSala, cartelera, CargarSucursales, SeleccionarSucursal, ReservaDeButacas
import random


def inicio():
    print("-" * 40)
    print("|      🎥 Bienvenido a CineUADE 🎥      |")
    print("-" * 40)

def main():

    Menu=0
    while Menu==0:
        dni=int(input("ingrese su DNI sin puntos: "))
        while dni < 1000000 or dni > 99999999:
            dni=int(input("ingrese su DNI sin puntos: "))
        print(cartelera())
        Opciones= 1 #int(input("ingrese el numero de la opcion que quiere (1-3) "))
        while Opciones > 3 or Opciones < 1: 
            print("el numero tiene que estar en un rango de 1 a 3")
            Opciones=int(input("ingrese el numero de la opcion que quiere (1-3) "))

        if Opciones == 1:#esta misma base va en las de abajo
            print("se selecciono la opcion 1 compra entrada")
            print("ingresa -1 para volver para atras")
            print("")
            Preguntar = int(input("quieres volver al menu"))
            while 1 != Preguntar != -1:
                print("-1")
                Preguntar = int(input("quieres volver al menu"))
            if Preguntar == -1:
                print("moris")
                Menu=0
            else:
                CargarSucursales()
        if Opciones == 2:
            print("selecciono opcion 2")
            Menu=0
        if Opciones == 3:
            print("selecciono opcion 3")
            if Opciones == -1:
                Menu=0

if __name__ == "__main__":
    inicio()
    main()