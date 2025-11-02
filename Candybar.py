def compracandybar():
    Productos=CargarCandy()
    print("Candy Bar")
    print("Opciones de productos:")
    print(Productos.keys)





def CargarCandy():
    Arch=open("CandybarProdutos.cvs", mode="wt", encoding="utf-8")
    productosCandy={}
    for linea in Arch:
        prod=linea.strip().split("/")
        Specs={"precio":int(prod[1]),"stock":int(prod[2]),"id":prod[3]}
        productosCandy[prod[0]]=Specs
        
    Arch.close()
    return productosCandy

def guardar_candybar_en_archivo(candybar):
    with open("CandybarProdutos.cvs", mode="wt", encoding="utf-8") as arch:
        for producto, datos in candybar.items():
            linea = f"{producto}/{datos['Precio']}/{datos['Stock']}/{datos['ID']}\n"
            arch.write(linea)
    