def getData():
    import requests
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    data=response.json()
    return data
class CasaCambio:
    def __init__(self,valor_compra:float,valor_venta:float) -> None:
        self.venta=float(valor_venta)
        self.compra=float(valor_compra)
    def ComprarDolares(self,montoDolares)->float:
        return montoDolares*self.compra
    def VenderDolares(self,montoSoles)->float:
        return montoSoles/self.venta    
    def __str__(self) -> str:
        return f"el valor de la venta es S/. {self.venta} y de compra es S/. {self.compra}"
msg="""------------------------
CASA DE CAMBIO - SUNAT
1)Ver tipo de cambio
2)Comprar (Dólares → Soles)
3)Vender (Soles → Dólares)
4)Salir
"""
while(True):
    print(msg)
    opcion=int(input("ingrese una opción: "))
    data=getData()
    tc=CasaCambio(data['compra'],data['venta'])
    if opcion==1:
        print(tc)
    if opcion==2:
        print("A continuación esta entidad comprará tu dinero (dólares) y te pagará en soles ... ")
        Montocomprar=float(input("ingrese el monto a vender (dólares que venderá): "))
        montoCliente=tc.ComprarDolares(Montocomprar)
        print("Usted recibirá ",montoCliente," soles.")
    if opcion==3:
        print("A continuación esta entidad te venderá dólares, pagarás en soles  ... ")
        Montovender=float(input("ingrese el monto a comprar (soles a enviar): "))
        montoCliente=tc.VenderDolares(Montovender)
        print("Usted recibirá  ",montoCliente,"en dólares.")
    if opcion==4:
        pass
        print("Hasta luego.")
        break