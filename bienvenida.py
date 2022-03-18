def Bienvenida(email):
    print("Bienvenido/a al Sistema")
    con_bd = sqlite3.connect('base1.db')
    cursor_db = con_bd.cursor()
    sql = "SELECT Nombres, Edad, Telefono FROM  sistema WHERE Correo=?"
    cursor_db.execute(sql, (email,))
    fila = cursor_db.fetchone()
    if len(fila) > 0:
        if len(fila) > 0:
            print(fila[0])
        if len(fila) > 0:
            print("Su telefono",fila[2])
            print("Su edad es",fila[1])
        return
    
    

