from funciones_cine import MostrarSala, cartelera, CargarSucursales, SeleccionarSucursal, ReservaDeButacas, PrecioDelaEntrada, comprobante
import random


def inicio():
    print("-" * 40)
    print("|      🎥 Bienvenido a CineUADE 🎥      |")
    print("-" * 40)

def main():
    dni = int(input("Ingrese su DNI: "))
    while dni < 1000000 or dni > 99999999:
        dni = int(input("DNI inválido. Ingrese su DNI nuevamente: "))
    print(" ")
    cartelera()
    print(" Seleccione la película que desea ver ")
    pelicula = int(input("Ingrese el número de la película: ")).lower().strip()
    while pelicula < 1 or pelicula > 4:
        pelicula = int(input("Número inválido. Ingrese el número de la película nuevamente: "))
    print(" ")
    print("Usted seleccionó la película:", pelicula)
    print(" ")
    formato()
    formato = int(input("Ingrese el número del formato (1 a 3): "))
    while formato < 1 or formato > 3:
        formato = int(input("Número inválido. Ingrese el número del formato nuevamente: "))
    print(" ")
    print("Seleccione la sucursal y Sala")
    SucursalAbasto, SucursalCaballito, SucursalPalermo = CargarSucursales()
    SeleccionarSucursal(SucursalAbasto, SucursalCaballito, SucursalPalermo)
    print("Precio de la entrada")
    PrecioDelaEntrada()
    print(" ")
    print("Gracias por su compra. ¡Disfrute la película!")
    print(" ")
#Comprobante : Falta arreglar lo de la sucursal y precio final
#Falta: Lambda, Slices, Funcion del lenguajes, informe de ventas

    

   

if __name__ == "__main__":
    inicio()
    main()