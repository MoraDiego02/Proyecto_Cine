def inicio():
    print("-" * 40)
    print("|      🎥 Bienvenido a CineUADE 🎥      |")
    print("-" * 40)
    print("| Instrucciones:                        |")
    print("| -                                     |")
    print("| -                                     |")
    print("| -                                     |")
    print("| -                                     |")
    print("-" * 40)

def main():
    eleccion = input("Que pelicula desea ver?: (Para ver el listado de las peliculas solo escriba 'peliculas') ").lower().strip()
    if eleccion == "peliculas":
        from funciones_cine import peliculas
        peliculas()
if __name__ == "__main__":
    inicio()
    main()