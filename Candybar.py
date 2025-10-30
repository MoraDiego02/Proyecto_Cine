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
                        precioproducto=Cantidad*candybar[Productoacomprar]["Precio"]
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



candybar={"Pepsi":{"Precio":300,"Stock":40,"ID":"1111"},
          "Pochoclo":{"Precio":200,"Stock":50,"ID":"2222"},
          "Agua":{"Precio":150,"Stock":30,"ID":"3333"},
          "Galletitas":{"Precio":250,"Stock":20,"ID":"4444"},
          "Nachos":{"Precio":100,"Stock":60,"ID":"5555"}
          }

registrocandy=compracandybar(candybar)