def mayor_valor(num1,num2):
    nummayor=0
    if num1 >num2:
        nummayor=num1
    else:
        nummayor=num2
    return nummayor
num1=float(input("Ingresa un primer número: "))
num2=float(input("Ingresa un segundo número: "))
numero_mayor=mayor_valor(num1,num2)
print("El mayor valor de los números es ", numero_mayor)