def compracandybar(candybar):
    print("Candy Bar")
    print("Opciones de productos:")
    for producto, detalles in candybar.items():
        print(f"{producto} - Precio: {detalles['Precio']}")
    preciototal=0
    registro_compras={}
    while True:
        Productoacomprar=input("Ingrese el nombre del producto que desea comprar (Ingrese 'Salir' para salir): ").strip().title()
        if Productoacomprar == "Salir":
            break
        try:
            if Productoacomprar in candybar:
                while True:
                    try:
                        Cantidad=int(input(f"Ingrese la cantidad de {Productoacomprar} que desea comprar: "))
                        if Cantidad < 1 or Cantidad > candybar[Productoacomprar]["Stock"]:
                            raise IndexError
                        precioproducto =Cantidad * candybar[Productoacomprar]["Precio"]
                        print("El precio de lo seleccionado es: ", precioproducto)
                        candybar[Productoacomprar]["Stock"] -= Cantidad
                        preciototal+=precioproducto
                        if Productoacomprar in registro_compras:
                            registro_compras[Productoacomprar]["Cantidad"] += Cantidad
                            registro_compras[Productoacomprar]["Subtotal"] += precioproducto
                        else:
                            registro_compras[Productoacomprar] = {"Cantidad": Cantidad,
                                                                "Subtotal": precioproducto
                                                         }
                        break
                    except IndexError:
                        print("Stock insuficiente para la compra.")
                    except ValueError:
                        print("Ingrese una cantidad válida.")
            else:
                raise ValueError
        except ValueError:
            print("El producto ingresado no se encuentra en la lista de productos disponibles.")
            continue

    print("\n--- Resumen de compra ---")
    for producto, datos in registro_compras.items():
        print(f"{producto}: {datos['Cantidad']} unidades - Subtotal: ${datos['Subtotal']}")
    print()
    print("El resumen de su compra es: ","$",preciototal)

    comprobantecandy = {"Productos": registro_compras, "Total": preciototal}
    return comprobantecandy 
    registrocandy=compracandybar(candybar)


def CargarCandy():
    Arch=open("CandybarProdutos.cvs", mode="wt", encoding="utf-8")

    


def guardar_candybar_en_archivo(candybar):
    """
    Guarda el diccionario de productos en el archivo.
    """
    with open("CandybarProdutos.cvs", mode="wt", encoding="utf-8") as arch:
        for producto, datos in candybar.items():
            linea = f"{producto}/{datos['Precio']}/{datos['Stock']}/{datos['ID']}\n"
            arch.write(linea)

registrocandy=compracandybar(candybar)