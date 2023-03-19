#EJERCICIO 2
class Producto:
    nombre=""
    marca=""
    precio=""
    def __init__(self,nombre, marca, precio):
        self.nombre= nombre
        self.marca=marca
        self.precio=precio
    def __str__(self):
        return f'Producto: {self.nombre} -- Marca: {self.marca} -- Precio: S/. {self.precio}'

class Catalogo:
    autopartes=[]
    def __init__(self):
        self.autopartes=[]
    def agregar(self,p=Producto):
        self.autopartes.append(pxt)
    def mostrar(self):               
        if len(self.autopartes)>0:
            print("""----------------------------
            PRODUCTOS DE CATÁLOGO DE AUTOPARTES""")
            for i in self.autopartes:
                  print (i)
        else:
             print ("No se encontró productos en el catálogo.")
              
ctl= Catalogo()
msg="""--------------------------------
CATÁLOGO DE AUTOPARTES"""
opciones= """1) Agregar productos
2) Mostrar productos
3) Salir
Elije la opción que deseas realizar: """
while True:    
    print(msg)
    opcion=int(input(opciones))
    if opcion==1:
        try:
            nombre=input("Ingresa el nombre del producto: ")
            marca=input("Ingresa la marca del producto: ")
            precio=float(input("Ingresa el precio del producto (en soles): "))
            pxt=Producto(nombre, marca, precio)
            ctl.agregar()
        except Exception as Error:
                print("error: ", Error)
        else:
                print("*** producto agregado")
    elif opcion==2:
        try: 
            ctl.mostrar()
        except:
             print("Sucedió un error")
    elif opcion == 3:
         print("Muchas gracias, hasta luego.")
         break         
    else:
         print("Opción no encontrada")
       