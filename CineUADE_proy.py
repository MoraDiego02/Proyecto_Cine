from funciones_cine import cartelera, formato, CargarSucursales, SeleccionarSucursal, PrecioDelaEntrada, comprobante, FinDelDia

def inicio():
    print("-" * 40)
    print("|      🎥 Bienvenido a CineUADE 🎥      |")
    print("-" * 40)

def main(sucursales):
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