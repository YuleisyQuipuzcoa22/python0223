class Producto:
    nombre =""
    codigo = ""    
    def __init__(self,nombre, codigo):
        self.nombre= nombre
        self.codigo = codigo        
    def __str__(self):
        return f'NOMBRE DEL PRODUCTO: {self.nombre.upper()} ---- CÓDIGO: {self.codigo.upper()}'
class Code:
    def Especification(self, p=Producto):       
        pais= (codigo[: codigo.find("-")])
        lote= (codigo[codigo.find("-")+1:codigo.rfind("-")])
        print("""-------------------------------------------
ESPECIFICACIONES DEL CÓDIGO DE PRODUCTO
-------------------------------------------""")
        print("PAÍS DE ORIGEN: ", pais.upper())
        print("NÚMERO DE LOTE: ",lote)
c=Code()
nombre=input("Ingresa el nombre del producto: ")
codigo=input("Ingresa el codigo del producto (PAIS-LOTE-AÑO): ")
px=Producto(nombre,codigo)
try:
    print("•••••••••••••••••••••••••••••••••••••••")
    print(px)
    c.Especification()
except:
    print("Sucedió un error.")
else:
    import os
    print(os.getcwd())
finally:
    print("proceso terminado")

