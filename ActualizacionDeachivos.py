def AdministrarArchivos(Info,Op):
    if Op == 1 :#este es para añadir el usuario a la base de datos 
        arch=open("cuentas.cvs",mode="at")
        arch.write(Info)
        arch.close
        return
    if Op == 2:#este va a ser el de cambiar la contraseñe 
        arch=open("cuentas.cvs", mode="rt")
    if Op == 3:#este añadir las finanzas de fin del dia
        arch=open("FinanzasFinDeDia.cvs", mode="at")
    else:
        print("te re pasaste papai")
