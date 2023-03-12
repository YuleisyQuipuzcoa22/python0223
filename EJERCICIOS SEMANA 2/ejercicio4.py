import sys
def imprimir_argumentos():
    arg = sys.argv[1:]
    print("Los argumentos ingresados son: ")
    for argumento in arg:
        print(argumento)
imprimir_argumentos()