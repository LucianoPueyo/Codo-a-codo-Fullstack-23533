try:
    print("Me conecto a una BBDD")
    print(7/0)
except:
    print("UPS ocurrio un error")

finally:
    print("Me desconecto de BBDD")