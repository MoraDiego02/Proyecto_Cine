from funciones_cine import MostrarSala, cartelera, CargarSucursales, SeleccionarSucursal, ReservaDeButacas, PrecioDelaEntrada, comprobante, formato, FinDelDia
import random


def inicio():
    print("-" * 40)
    print("|      🎥 Bienvenido a CineUADE 🎥      |")
    print("-" * 40)

def main():
    Seguir = "si"
    Sucursales = CargarSucursales()
    while Seguir.lower() == "si":
        dni = int(input("Ingrese su DNI: "))
        while dni < 10000000 or dni > 99999999:
            dni = int(input("DNI inválido. Ingrese su DNI nuevamente: "))
        print(" ")
        cartelera()
        print(" Seleccione la película que desea ver ")
        pelicula = int(input("Ingrese el número de la película: "))
        while pelicula < 1 or pelicula > 4:
            pelicula = int(input("Número inválido. Ingrese el número de la película nuevamente: "))
        print(" ")
        print("Usted seleccionó la película:", pelicula)
        print(" ")
        formato()
        print(" ")
        print("Seleccione la sucursal y Sala")
        Sucursales = CargarSucursales()
        SeleccionarSucursal(Sucursales)
        
        print(Sucursales)
        print("Precio de la entrada")
        PrecioDelaEntrada()
        print(" ")
        print("Gracias por su compra. ¡Disfrute la película!")
        print(" ")
        comprobante(dni, pelicula)
        Seguir = input("¿Desea realizar otra compra? (si/no): ").lower()
            
    
        
    print("¡Hasta luego!")      
    FinDelDia(Sucursales)

if __name__ == "__main__":
    inicio()
    main()