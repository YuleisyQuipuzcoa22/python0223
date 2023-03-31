import pandas as pd
import sqlite3
conn=sqlite3.connect('registroprofesion.db')
cur=conn.cursor()
url="C:\\Users\\yulei\\Desktop\\WORKSPACEPYTHON\\SEMANA 5\\EJERCICIO FINAL\\titanic.csv"
df= pd.read_csv(url)
class Titanic:    
    def MostrarTablaTic():
        print( df)
    def TiposdeData():
        print(df.dtypes)
    def ColumnaEsp():
        print(" *** Estos son los títulos de las columnas:")
        for c in df.columns:
            print(c)
        clms=input(" --- Ingresa la columna que deseas visualizar: ")
        try:
            print(df[clms].head())
        except:
            print("Esta columna no existe")
    def DatEstadis():
        print(df.describe())
    def AñadirColumna():
        data=input ("Ingresa lo que quieres que aparezca en toda la columna: ")
        df['Nueva columna']= data
        print(df.head())
class Tablas:
    def crear_table():              
        cur.execute("CREATE TABLE IF NOT EXISTS ESTUDIANTES (Nombre TEXT,Edad INTERGER, Carrera TEXT)")
        conn.commit()

    def insertar_data():
            cant= int(input("Ingrese la cantidad de datos a registrar: "))            
            for i in range(cant):
                name=input("Ingrese nombre: ")
                edad= int(input("Ingrese edad: "))
                carrera= input("ingrese su carrera profesional: ")
                print( "--------------------------------------------")
                cur.execute("insert into ESTUDIANTES values(?,?,?)",(name,edad,carrera))
                conn.commit()

    def mostrar_tabla():
            cur.execute("SELECT * FROM ESTUDIANTES")
            x= cur.fetchall()            
            for i in x:
                 print(i)
                 


            

       