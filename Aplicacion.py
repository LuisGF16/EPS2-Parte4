import sqlite3

#
conexion = sqlite3.connect("AGLR_almacen.db")

def listar_base():
    consulta_listar = """ SELECT*FROM PRODUCTO"""
    cursor.execute(consulta_listar)
    productos = cursor.fetchall()
    print("ID  CODIGO  NOMBRE  PRECIO")
    for producto in productos:
        print (producto)
    
    conexion.commit()
    return producto

    
cursor = conexion.cursor()

if conexion:
    while True:
        print ("\n*Menu*")
        print ("1. Registrar")
        print ("2. Eliminar")
        print ("3. Editar")
        print ("4. Listar")
        print ("5. Salir")
        
        opc = input ("Ingrese un opcion: ")
        
        if opc == "1":
            
            codigo = input("Ingrese el codigo del pruducto: ")
            nombre = input("Ingrese el nombre del pruducto: ")
            precio = input("Ingrese el precio del pruducto: ")
            
            lista_ingresar = [(codigo, nombre, precio)]
            consulta_ingresar = """ INSERT INTO PRODUCTO (CODIGO, NOMBRE, PRECIO) VALUES (?,?,?)"""
            cursor.executemany(consulta_ingresar, lista_ingresar)
            conexion.commit()        
        elif opc == "4":
            print ("INDICE - ")
            listar_base()  
        elif opc == "5":
            break
        else:
            print ("Opcion invalida")
        
else:
    
    cursor.execute(tabla_producto)
    conexion.close()