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

def compraCandybar():
    total_candy = 0.0
    try:
        while True:
            mostrarProductos()  

            producto_id = estaEntre(1, 5, "\nSeleccione el producto a comprar (1-5): ")

            item = None
            with open("archivosDeTexto/CandybarProductos.csv", "r", encoding="utf-8") as arch:
                for linea in arch:
                    linea = linea.strip()
                    if not linea:
                        continue
                    id_str, nombre, precio_str, stock_str = linea.split(";")
                    if int(id_str) == producto_id:
                        item = {"id": int(id_str), "nombre": nombre,
                                "precio": float(precio_str), "stock": int(stock_str)}
                        break
            if item is None:
                print("Producto inexistente.")
                continue

            cant = estaEntre(1, item["stock"], f"Ingrese la cantidad de {item['nombre']} (1-{item['stock']}): ")
            subtotal = item["precio"] * cant

            conf = validarString(("s","si","n","no"),
                                 f"El costo es ${subtotal:.2f}. ¿Confirmar compra?: ")
            if conf in ("s","si"):
                actualizarCandybar(item["id"], cant)   
                total_candy += subtotal

            otra = validarString(("s","si","n","no"), "¿Desea realizar otra compra?: ")
            if otra not in ("s","si"):
                break
    except (IOError, OSError):
        print("Error al abrir el archivo.")
    return total_candy

def mostrarProductos():
    try:
        print("\nID  | Nombre                 | Precio   | Stock")
        with open("archivosDeTexto/CandybarProductos.csv", "r", encoding="utf-8") as arch:
            for linea in arch:
                linea = linea.strip()
                if not linea:
                    continue
                id_str, nombre, precio_str, stock_str = linea.split(";")
                print(f"{int(id_str):<3} | {nombre:<22} | ${float(precio_str):>7.2f} | {int(stock_str):>5}")
    except (IOError, OSError):
        print("Error al abrir el archivo.")