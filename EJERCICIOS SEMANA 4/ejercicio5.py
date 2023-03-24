
import re
def Validarnumtelef():
    regla= r"^9\d*$"
    if re.findall(regla, num):
        cant = len(num)
        if cant == 9:
            print(" --- Número telefónico de celular correcto.")
        else:
            print(" ---- Número telefónico de celular incorrecto.")
    else:
        print(" *** El número teléfonico ingresado no inicia con 9.")

print("VALIDA AQUÍ TU NÚMERO TELEFÓNICO DE CELULAR")
num = input("Ingresa tu número telefónico de celular: ")
Validarnumtelef()