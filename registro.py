from ast import Return
import os
import sqlite3
from login import login


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


BASE_DIR= os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.db")


def bootstrap():
    menu= input("Elija la Opcion")
    print("Ingrese 1 para Registrarse")
    print("Ingrese 2 para Iniciar Seccion")
    if menu =="1":
        registro()
    if menu =="2":
        login()


def registro():
    correo= str(input("Ingrese su correo"))
    contrasena= str(input("Ingrese su contrasena"))
    nombres= str(input("Ingrese sus Nombres"))
    telefono= int(input("Ingrese su Telefono"))
    cuidad= str(input("Ingrese su Cuidad"))
    edad= int(input("Ingrese su Edad"))

    verificacion=input("Sus datos son correctos?")
    if verificacion == "si":
            con_bd = sqlite3.connect('base1.db')
            cursor_db = con_bd.cursor()
            sql = "INSERT INTO sistema(Correo, Edad, Contrasena, Nombres, Telefono, Ciudad ) VALUES(?, ?, ?, ?, ?, ?)"
            cursor_db.execute(sql, (correo,edad,contrasena, nombres, telefono, cuidad))
            con_bd.commit()
            cursor_db.close()
            proveedor_correo = 'smtp.gmail.com: 587'
            remitente ='gomeloslos8@gmail.com'
            password ='1004871606'
            servidor = smtplib.SMTP(proveedor_correo)
            servidor.starttls()
            servidor.ehlo()
            servidor.login(remitente, password)
            mensaje = "<h1>Bievenido a nuestra Plataforma de  Tursismo Sueña</h1>"
            msg = MIMEMultipart()
            msg.attach(MIMEText(mensaje,'html'))
            msg['From'] = remitente
            msg['To'] = correo
            msg['Subject'] = 'Registro Exitoso'
            servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

            iniciologin= input("Su Registro fue Exitoso ¿Desea Iniciar Seccion?")
            if iniciologin == "si":
                return login()
            else:
                return bootstrap()
                
                
    return login()
    









