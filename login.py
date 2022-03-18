from bienvenida import Bienvenida


import os
import sqlite3


def login():
    correo=input("Ingrese su Correo")
    contrasena=input("Ingrese su Contrasena")
    
    con_bd = sqlite3.connect('base1.db')
    cursor_db = con_bd.cursor()
    sql = "SELECT Contrasena, Nombres  FROM  sistema WHERE Correo=?"
    cursor_db.execute(sql, (correo,))
    fila = cursor_db.fetchone()
    
    if fila is not None:
        if contrasena == fila [0]:
            return Bienvenida(correo)
        else:
            print("Correo o Contrasena Incorrecta")

