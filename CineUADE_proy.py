from funciones_cine import cartelera, formato, CargarSucursales, SeleccionarSucursal, PrecioDelaEntrada, comprobante, FinDelDia
from Usuarios import RegistroDeUsuario
from ActualizacionDeArchivos import VerificarRoleDeUsuario
def inicio():
    print("-" * 40)
    print("|      🎥 Bienvenido a CineUADE 🎥      |")
    print("-" * 40)

def main():
    print("ingrese el numero de la opcion que quiere seleccionar")
    print("1 iniciar Sesion ")
    print("2 Crear una cuenta ")
    print("3 reservar una pelicula ")
    while True:
        try:
            Opcion=int(input("ingrese el numero de la opcion que quiere elegir: "))
            if Opcion < 1 or Opcion > 3:
                raise ValueError
            else:
                break
        except ValueError:
            print("ingrese 1 al 3 segun la opcion que quiere")
    
    
    if Opcion== 1:
        Usuario=RegistroDeUsuario(Opcion)
    if Opcion == 2:
        RegistroDeUsuario(Opcion)

    VerificarRoleDeUsuario(Usuario)
    

if __name__ == "__main__":
    inicio()
    sucursales = CargarSucursales()
    main()