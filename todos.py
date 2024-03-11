# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 07:48:30 2024

@author: quigo
"""

import menu

class Producto:
    #crear los objetos de tipo producto
    def __init__(self, id, nombre, descripcion, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        
    def __str__(self):
        return f"Producto: {self.nombre} - ID: {self.id}- Descripcion:{self.descripcion}-Cantidad:{self.cantidad}-Precio:${self.precio}"
    
    
productos=[]

while True:
    menu.menux()
    try:
        opcion= int(input("Ingrese la opcion deseada="))
    
        
        if opcion==1:
            print()
            print("Ingresar datos del producto al ingresar")
            idx=int(input("Ingrese el id del producto="))
            nombre=input("Ingrese el nombre del producto=")
            descripcion=input("Ingrese la descripcion del producto=")
            cantidad=int(input("Ingrese cantidad del producto="))
            precio=int(input("Ingrese el precio del producto="))
            producto_nuevo=Producto(idx, nombre, descripcion, cantidad, precio)
            productos.append(producto_nuevo)
            # producto1=producto.Producto(1, "Producto 1", "Descripción del producto 1", 10, 100)
            # productos.append(producto1)
            print()
        if opcion==2:
            print("Opcion 2")
        if opcion==3:
            print("Opcion 3")
        if opcion==4:
            print("Opcion 4")
        if opcion==5:
            print("Lista de productos")
            for j in range(len(productos)):
                print("Id:",productos[j],id )
                print("Nombre:",productos[j],nombre )
                print("Descripcion:",productos[j],descripcion )
                print("Cantidad:",productos[j],cantidad )
                print("Precio:",productos[j],precio )
        if opcion==6:
            print("Opcion 6")
            break
        else:
            print("Opcion no deseada ingrese del 1 al 6")
    except ValueError:
         print("Ingrese un número entero")
        
