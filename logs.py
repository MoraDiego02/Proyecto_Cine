from datetime import datetime 


def log (Info, FFuncion, ):
    fecha=datetime.now()
    fecha=fecha.strftime("%d/%m/%Y %H:%M:%S")
    print(fecha)
    with open("log.txt", mode="a" ,encoding="utf-8") as arch:
        print("nashe")