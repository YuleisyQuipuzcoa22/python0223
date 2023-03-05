#QUIPUZCOA LOPEZ YULEISY
# Realice un programa que calcule la suma de los números hasta el valor ingresado.
# Primera manera:
num= int(input("Ingresa un número entero: "))
suma = int((num/2)*(1+num))
print("La suma de los números hasta el valor ingresado es: ", suma)
print("------------------------------------------")
#Segunda manera:
num= int(input("Ingresa un número entero: "))
suma=1
for i in range(0,num-1,1):
      if(i<num):
            suma= suma + ((i+1)+1)
            i+=1
print("La suma de los números hasta el valor ingresado es: ", suma)