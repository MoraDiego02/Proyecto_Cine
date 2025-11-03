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
            filas = []
            with open("archivosDeTexto/CandybarProductos.csv", "r", encoding="utf-8") as arch:
                for linea in arch:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(";")
                    if len(partes) < 3:
                        continue
                    id_str, nombre, precio_str = partes[0], partes[1], partes[2]
                    stock_str = partes[3] if len(partes) > 3 else "999"

                    try:
                        precio = float(precio_str.replace(",", "."))
                        _id = int(id_str)
                        stock = int(stock_str)
                    except ValueError:
                        continue

                    filas.append((_id, nombre, precio, stock))

            if not filas:
                print("No hay productos disponibles en el Candy Bar.")
                return total_candy

            print("\nID  | Nombre                 | Precio   | Stock")
            for _id, nombre, precio, stock in filas:
                print(f"{_id:<3} | {nombre:<22} | ${precio:>7.2f} | {stock:>5}")

            try:
                producto_id = int(input("\nIngrese el ID del producto: ").strip())
            except ValueError:
                print("ID inválido.")
                continue

            item = next((r for r in filas if r[0] == producto_id), None)
            if item is None:
                print("Producto inexistente.")
                continue

            _id, nombre, precio, stock = item
            if stock <= 0:
                print("Sin stock.")
                continue

            try:
                cantidad = int(input(f"Ingrese la cantidad de {nombre} (1-{stock}): ").strip())
                if cantidad < 1 or cantidad > stock:
                    raise ValueError
            except ValueError:
                print("Cantidad inválida.")
                continue

            subtotal = precio * cantidad

            resp = input(f"El costo es ${subtotal:.2f}. ¿Confirmar compra? (si / no): ").strip().lower()
            if resp in ("s", "si"):
                try:
                    actualizarCandybar(_id, cantidad)
                except Exception:
                    pass
                total_candy += subtotal
            else:
                print("Compra cancelada para este producto.")

            otra = input("¿Desea realizar otra compra? (si o no): ").strip().lower()
            if otra not in ("s", "si"):
                break

    except (IOError, OSError):
        print("Error al abrir el archivo del candybar.")

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