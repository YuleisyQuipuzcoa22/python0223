#QUIPUZCOA LOPEZ YULEISY
#manera 1
dic = {
    "nombre del curso": "",
    "cantidad de alumnos": 0, 
    "activo": False, 
    "nombre de profesor": "", 
    "max nota": 0,
    "alumnos": []
    }

dic["nombre del curso"] = input("Ingrese el nombre del curso: ")
dic["cantidad de alumnos"] = int(input("Ingrese la cantidad de alumnos: "))
dic["activo"] = bool(input("¿El curso está activo? (True o False): "))
dic["nombre de profesor"] = input("Ingrese el nombre del profesor: ")
dic["max nota"] = float(input("Ingrese la nota máxima: "))
dic["alumnos"] = input("Ingrese una lista de alumnos: ").split(",")

print("DICCIONARIO\n", dic)
#manera 2
listaNombre= []
cantalumnos= [0]
actv=[0]
nomprof=[]
notamax=[0]
alumnos=[]
dic = {
    "Nombre de curso": listaNombre,
    "Cantidad de alumnos": cantalumnos,
    "activo": actv, 
    "nombre de profesor": nomprof, 
    "max nota": notamax,
    "alumnos": alumnos,
    }
for i in range(0,3,1):
      if(i<3):
            nombre= input("Ingresa el nombre del curso: ")
            listaNombre.append(nombre)
            cantAlum= int(input("Ingrese la cantidad de alumnos: "))
            cantalumnos.append(cantAlum)
            act= bool(input("¿El curso está activo? (True o False): "))
            actv.append(act)
            prof=input("Ingrese el nombre del profesor: ")
            nomprof.append(prof)
            nmax=input("Ingrese la nota máxima: ")
            notamax.append(max)
            listalum= input("Ingrese una lista de alumnos: ").split(",")
            alumnos.append(listalum)
print(dic)

