#crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3 as sql

def createDB():
    conn = sql.connect("Alumnos.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Alumnos(
            nombre text,
            apellido text,
            id integer
            )"""
    )
    conn.commit()
    conn.close()
    
def insertRow(nombre, apellido, id):
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Alumnos VALUES ('{nombre}', '{apellido}', {id})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
def search():
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Alumnos WHERE nombre='Vanesa'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def deleteRow():
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM Alumnos WHERE nombre='Gabriel'"
    cursor.execute(instruccion)    
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    #createDB()
    #createTable()
    #insertRow("Gabriel", "Martínez", 25689784)
    #insertRow("Facundo", "Gonzalez", 25005384)
    #insertRow("Francisco", "Rodríguez", 22963417)
    #insertRow("Vanesa", "Quintana", 21559010)
    #insertRow("Yessica", "Mijares", 12360770)
    #insertRow("Mauricio", "Acosta", 14111258)
    #insertRow("Claudia", "Palacios", 26248715)
    #insertRow("Juan", "Millan", 11655070)
    search()
    #deleteRow()