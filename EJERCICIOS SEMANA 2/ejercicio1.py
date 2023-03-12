print("MENÚ ITERATIVO")
while True:
    print("---------------------------------------------")
    print("""¿Qué quieres hacer?
    1) Dibujar un cuadrado con ***
    2) Identificar si el número es múltiplo de 2
    3) Lista de elementos con nombres y edad, imprimir solo +18
    4) Salir""")   
    opcion=input("Ingresa una opción: ")
    if opcion=="1":
           for _ in range(6):
            print('******')  
    elif opcion=="2":
        num=int(input("Ingresa un número para determinar si es múltiplo de 2: "))
        if num %2 == 0:
            print("El número ingresado es MÚLTIPLO DE 2")
        else:
             print("El número ingresado NO es MÚLTIPLO DE 2")
    elif opcion =="3":
        num=int(input("Ingrese el número de personas a registrar:"))
        list_name=[]
        list_year=[]          
        list_18=[]
        for i in range(1,num+1):
            nombre=input("Ingrese un nombre:")
            list_name.append(nombre)
            edad=int
            (input("Ingresa tu edad: "))
            list_year.append(edad) 
            if edad>=18:
                list_18.append(nombre)           
            pass   
        print("Las personas mayores de edad son: ", list_18)
    elif opcion== "4":
        print("¡Hasta luego!")
        break
    else:
        print("La opción ingresada no existe, vuelve a intentarlo")
            