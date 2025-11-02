
def reinicioDeContraseña():
    print("para poder autentificar que la cuenta es suya vamos a pedir los siguientes datos")
    arch = open("cuentas.cvs", mode="rt")
    Cuenta = False
    try:
        Usuario = input("ingrese el numero de usuario")
        for linea in arch:
            CuentaAux = linea.strip().split("/")
            if Usuario == CuentaAux[0]:
                Cuenta = CuentaAux
        if Cuenta == False:
            raise ValueError
    except ValueError:
        print("ese nombre de usuario no pertenece a ninguna cuenta")
    else:
        UsuarioNom = Cuenta[0]
        Errores = 3    
        try:
            if Errores == 0:
                print("se a quedado sin intentos mande un mensaje a atencion al cliente")
                print("1. Si 2. No")
                try:
                    op=int(input("seleccione la opcion que quiere"))
                    if op < 1 and op > 2:
                        raise ValueError
                except ValueError:
                    print("ingrese Un numero que este en las opciones")
                    if op == 1:
                        op=EnviarMensajeAAC()
                    if op == 2:
                        return   
            Dni = input("ingrese su Dni")
            if Dni == Cuenta [2] :
                print("el Dni es valido")
            else:
                raise ValueError
            
        except ValueError:
            print("el Dni no es valido")
            Errores -= 1
        else:
            arch.close()

            NuevaContraseña = SeguridadDeContraseña()
            Cuenta[1] = NuevaContraseña
        
            arch = open("cuentas.cvs", mode="r", encoding="utf-8")
            LineasActualizadas = [] 

            for linea in arch:
                datos = linea.strip().split("/")
            
                if datos[0] == Usuario:
                    nueva_linea = "/".join(Cuenta) + "\n"
                    LineasActualizadas.append(nueva_linea)
            
                else:    
                    LineasActualizadas.append(linea)
            arch.close()

            arch = open("cuentas.cvs", mode="w", encoding="utf-8")

            for linea in LineasActualizadas:
                arch.write(linea)

            arch.close()
            print("Contraseña actualizada correctamente.")
                
            log("reiniciodecontraseña",3,UsuarioNom)
            return 
