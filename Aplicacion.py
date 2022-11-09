import sqlite3


conexion = sqlite3.connect("AGLR_almacen.db")
tabla_producto = """
                        CREATE TABLE PRODUCTO(
                        IDPRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT,
                        CODIGO TEXT UNIQUE,
                        NOMBRE TEXT,
                        PRECIO REAL)
                    """
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
        
        
else:
    
    cursor.execute(tabla_producto)
    conexion.close()