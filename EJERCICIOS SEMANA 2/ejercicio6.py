def main():
    evento = obtenerEvento()
    confirmacion= validación(evento)
    procesar(evento, confirmacion)

def obtenerEvento():
    evento =(input("Ingrese el NOMBRE del evento: "))
    print("""-Fiesta
             -Concierto
             -Cine""")
    return evento

def validación(evento):
    eventos = ["Fiesta","Concierto","Cine"]
    evento=evento.capitalize()
    if evento in eventos:
        print("El evento ingresado se encuentra disponible")
        confirmacion= 1 
    else:
        print("El evento ingresado no se encuentra en las opciones.")
        confirmacion=0
    return confirmacion

def procesar(evento, confirmacion):
    if confirmacion==1:
         print(f"El Evento al que asistirás será: {evento}...")
    elif confirmacion==0:
        print("Por el momento, no asistirás a algún evento...")
    
main()
