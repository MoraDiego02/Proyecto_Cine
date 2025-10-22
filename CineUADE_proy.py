from funciones_cine import cartelera, formato, CargarSucursales, SeleccionarSucursal, PrecioDelaEntrada, comprobante, FinDelDia
from Usuarios import
def inicio():
    print("-" * 40)
    print("|      🎥 Bienvenido a CineUADE 🎥      |")
    print("-" * 40)

def main(sucursales):
    print("ingrese el numero de la opcion que quiere seleccionar")
    print("1 iniciar Sesion/Crear una cuenta")
    print("2 reservar una pelicula")
    while True:
        try:
            Opcion=int(input(""))
            if Opcion != 1 or Opcion != 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("ingrese 1 o 2 segun la opcion que quiere")
    if Opcion== 1:
        Usuario=RegistroDeUsuario(Opcion)

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
    sucursal, sala = SeleccionarSucursal(sucursales)
    print("Precio de la entrada")
    PrecioDelaEntrada()
    print(" ")
    print("Gracias por su compra. ¡Disfrute la película!")
    print(" ")
    volver_a_comprar = input("¿Desea realizar otra compra? (si/no): ").lower()
    if volver_a_comprar == "si":
        main(sucursales)
    else:
        FinDelDia(sucursales)

if __name__ == "__main__":
    inicio()
    sucursales = CargarSucursales()
    main(sucursales)