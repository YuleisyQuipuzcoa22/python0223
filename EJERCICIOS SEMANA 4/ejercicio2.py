import random
class Sorteo:    
    vmax = 0
    cant = 0
    def __init__(self, vmax, cant) -> None:
       self.cant= cant
       self.vmax= vmax
       pass            
    
class Metodos:
    valores= []
    def SorteoNumerosLista(self,sorte=Sorteo): 
        self.valores= []             
        for i in range(0,cant,1):
            num =(random.randint(1,vmax))
            self.valores.append(num)
    def MostrarLista(self,sorte=Sorteo):
       print("Lista de valores sorteados → ", self.valores)
    def ValorAleatorio(self,sorte = Sorteo):
        print("Valor aleatorio --> ", random.choice(self.valores))
m= Metodos()
print( """
GENERA TU PROPIO SORTEO ( números enteros)
↓ Define tu cantidad y valores de números a sortear
↓ Mostrar lista de valores sorteados
↓ Escoger valor alatorio de la lista
""")
cant= int(input("Ingresa la cantidad de números a sortear: "))
vmax= int(input("Ingresa el valor máximo de lista: "))
sort=Sorteo(vmax, cant)
m.SorteoNumerosLista()    
m.MostrarLista()
while True:
    print("""
¿Qué desea realizar?    
1) Obtener valor aleatorio de lista generada.
2) Salir""")
    opcion= int(input("Ingrese una opción:"))
    if opcion== 1:
        m.ValorAleatorio()    
    elif opcion== 2:
        print("Hasta luego.")
        break
    else:
        print("Opción no encontrada.")
        

   