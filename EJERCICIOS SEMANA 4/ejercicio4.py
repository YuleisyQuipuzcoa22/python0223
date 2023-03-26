from datetime import datetime

class Registro:        
    def CrearArchivo():
        nombre = input("Ingrese el nombre del archivo a crear: ")
        archivo = open(nombre,'w')
        archivo.write('')
        print("El archivo ha sido creado con éxito ...")  
    
        mensaje = input("Ingrese algún mensaje: ")
        fecha = datetime.now()
        hoy = fecha.strftime("%d/%m/%Y %H:%M:%S")
        mostrar=archivo.write(f"{hoy} - Nombre de archivo: {nombre} - Mensaje: {mensaje}")
    
        archivo = open(nombre,'r')
        value= archivo.read(mostrar)
        print(value)
        archivo.close()  
    
    CrearArchivo()

    