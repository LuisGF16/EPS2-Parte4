# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
while True:
    print ("\n**Menu**")
    print ("1. Registrar")
    print ("2. Eliminar")
    print ("3. Editar")
    print ("4. Listar")
    print ("5. Salir")
    
    opc = input ("Ingrese un opcion: ")
    
    if opc == "1":
        print ("OPCION REGISTRAR")
    elif opc == "2":
        print ("OPCION ELIMINAR")
    elif opc == "3":
        print ("OPCION EDITAR")
    elif opc == "4":
        print ("OPCION LISTAR")
    elif opc == "5":
        break
    else:
        print ("Opcion invalida")