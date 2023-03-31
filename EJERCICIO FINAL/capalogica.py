from capamodelo import *
#from capamodelo2 import *
msjTi ="""
1) Mostrar Tabla Titanic
2) Mostrar tipo de datos de la tabla
3) Mostrar una columna en específico (los primeros datos)
4) Datos estadísticos ( promedio, mínimo, máximo, etc)
5) Añadir una columna
6) Salir
"""
msjTab =""" 
1) Ingresar datos
2) Mostrar Tabla
3) Salir
"""
def consultar(opcion:int):
    match opcion:
        case 1:
            while True:
                print(msjTi)
                op= int(input("Ingrese la opción de su preferencia: "))
                match op:
                    case 1:
                        Titanic.MostrarTablaTic()                    
                    case 2:
                        Titanic.TiposdeData()
                    case 3:
                        Titanic.ColumnaEsp()
                    case 4:
                        Titanic.DatEstadis()
                    case 5:
                        Titanic.AñadirColumna()
                    case 6:
                        print( "Hasta luego...")
                        break
                    case _:
                        print("Opción inexistente.")
            
        case 2:
            while True:
                Tablas.crear_table()                          
                print(msjTab)
                op= int(input("Ingrese la opción de su preferencia: "))
                match op:
                    case 1:
                        Tablas.insertar_data()
                        print("Se han registrado los datos corectamente ...") 
                    case 2:
                        Tablas.mostrar_tabla()
                    case 3:
                        print("Hasta luego ...")
                        break 
                    case _:
                        print("Esta opción no existe.")
                    
