biblioteca={
    "categorias": [
      {
        "Número de categorías":" ",
        "Categorías":" ",       
      }
    ],
    "libros":[
        {
            "nombrelibro":" ",
            "autor":" ",            
        }],
    "usuarios":[
        {
            "nombrecompleto": "",
        }
    ],
}
def categoriasLibros():
    listcateg=[]
    num= int(input("Ingrese el número de categorías: "))
    for num in range(1,num+1):
            categ=input("Categoría: ")
            listcateg.append(categ)
    dictCat={
          "Número de categorías": num,
          "Categorías": listcateg,
    }
    biblioteca["categorias"].append(dictCat)
def Libros():
    num=int(input("Ingrese la cantidad de libros:"))
    listaLibros=list()
    for i in range(1,num+1):
           nombreLibro=input("Nombre del libro: ")
           nombreAutor=input("Nombre del autor: ")
           libro=(nombreLibro,nombreAutor)
           listaLibros.append(libro)
    dictLibr={
            "nombrelibro":nombreLibro,
            "autor":listaLibros,            
    }
    biblioteca["libros"].append(dictLibr)

def DatosUsuario():
    listUsuario=[]
    num= int(input("Ingrese el número de usuarios: "))
    for num in range(1,num+1):
            nombre=input("Ingresa tu nombre: ")
            apellido=input("Ingresa tu apellido: ")
            nombrecompleto= nombre + apellido
            listUsuario.append(nombrecompleto)
    dictUsu={
         "nombrecompleto":nombrecompleto,
    }
    biblioteca["usuarios"].append(dictUsu)
categoriasLibros()
Libros()
DatosUsuario()    
print(biblioteca)