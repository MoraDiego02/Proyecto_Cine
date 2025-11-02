from ValidacionDeDatos import estaEntre, validarString

def actualizarCandybar(id,cantidad):
    try:
        with open("archivosDeTexto/CandybarProductosTemp.csv","w") as archTemporal:
            with open("archivosDeTexto/CandybarProductos.csv","r") as archViejo:
                for linea in archViejo:
                    archTemporal.write(linea)
        with open("archivosDeTexto/CandybarProductosTemp.csv","r") as archTemporal:
            with open("archivosDeTexto/CandybarProductos.csv","w") as archActualizado:
                for linea in archTemporal:
                    if linea[0] == id:
                        id,nombre,precio,stock = linea.split(";")
                        stock = int(stock)
                        archActualizado.write(f"{id};{nombre};{precio};{stock-cantidad}\n")
                    else:
                        archActualizado.write(linea)
        with open("archivosDeTexto/CandybarProductosTemp.csv","w"):
            pass
        print("Actualizacion de stock exitosa.")
    except (IOError, OSError):
        print("Error al abrir el archivo.")

def compraCandybar(compracandybar):
    try:
        with open ("archivosDeTexto/CandybarProductos.csv","r") as arch:
            producto = estaEntre(1,5,"\nSeleccione el producto a comprar (1-5): ")
            for linea in arch:
                if int(linea[0]) == producto:
                    id,nombre,precio,stock = linea.split(";")
                    precio, stock = int(precio),int(stock)
            cantidad = estaEntre(1,stock,f"Ingrese la cantidad de {nombre} a comprar (1-{stock}): ")
            total = precio*cantidad
            respuesta = validarString(("s","si","n","no"),f"El costo total es de ${total}. Desea realizar la compra?: ")
            if respuesta == "s" or respuesta == "si":
                actualizarCandybar(id,cantidad)
                compracandybar+=total
            compraMas = validarString(("s","si","n","no"),f"Desea realizar otra compra?: ")
            if compraMas == "s" or compraMas == "si":
                mostrarProductos(compracandybar)
            if compraMas == "n" or compraMas == "no":
                return compraCandybar

    except (IOError, OSError):
        print("Error al abrir el archivo.")

def mostrarProductos(Candycompra,seguir):
    try:
        with open ("archivosDeTexto/CandybarProductos.csv","r") as arch:
            for linea in arch:
                id,nombre,precio,stock = linea.split(";")
                print(f"{id}. {nombre} - ${precio}")
        compraCandybar(Candycompra)
    except (IOError, OSError):
        print("Error al abrir el archivo.")


