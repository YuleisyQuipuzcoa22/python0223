import os

def listar(path):
    elements = os.listdir(path)

    for elemento in elements:
        ruta = os.path.join(path, elemento)
        
        if os.path.isdir(ruta):
            print(f"Directorio -> {ruta}")
            listar(ruta)
        else:
            print(f"Archivo-> {ruta}")

listar(".")