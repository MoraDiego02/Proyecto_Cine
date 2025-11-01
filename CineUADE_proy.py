from funciones_cine import CargarSucursales 
from Usuarios import RegistroDeUsuario ,VerificarRoleDeUsuario
def inicio():
    print("-" * 40)
    print("|      🎥 Bienvenido a CineUADE 🎥      |")
    print("-" * 40)

def main():
    
    while True:
            
            Usuario=RegistroDeUsuario()
            VerificarRoleDeUsuario(Usuario)
        
            break

    print("fin del programa")
    


if __name__ == "__main__":
    inicio()
    sucursales = CargarSucursales()
    main()