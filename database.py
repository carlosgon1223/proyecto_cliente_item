import mysql.connector
from pydantic import BaseModel
from typing import List, Optional
import threading

db_lock = threading.Lock()

class Cliente(BaseModel):
    id: Optional[int] = None
    nombre_cliente: str
    correo: str

class Item(BaseModel):
    id: Optional[int] = None
    nombre: str
    codigo: str

db_connection = mysql.connector.connect(
    host="producciondb.mysql.database.azure.com",
    user="carlosgon",
    password="Qwezaxs1999",
    database="produccion_db"
)
db_cursor = db_connection.cursor()

def drop_cliente_table():
    with db_lock:
        db_cursor.execute('''DROP TABLE IF EXISTS clientes''')
        db_connection.commit()

def create_cliente_table():
    with db_lock:
        db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre_cliente VARCHAR(255) NOT NULL,
                correo VARCHAR(255) NOT NULL
            )
        ''')
        db_connection.commit()

def drop_item_table():
    with db_lock:
        db_cursor.execute('''DROP TABLE IF EXISTS items''')
        db_connection.commit()

def create_item_table():
    with db_lock:
        db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                codigo VARCHAR(255) NOT NULL
            )
        ''')
        db_connection.commit()

def insert_cliente(cliente: Cliente):
    with db_lock:
        query = "INSERT INTO clientes (nombre_cliente, correo) VALUES (%s, %s)"
        values = (cliente.nombre_cliente, cliente.correo)
        db_cursor.execute(query, values)
        db_connection.commit()

def insert_item(item: Item):
    with db_lock:
        query = "INSERT INTO items (nombre, codigo) VALUES (%s, %s)"
        values = (item.nombre, item.codigo)
        db_cursor.execute(query, values)
        db_connection.commit()

def get_all_clientes(skip: int = 0, limit: int = 10) -> List[Cliente]:
    with db_lock:
        db_cursor.execute("SELECT id, nombre_cliente, correo FROM clientes LIMIT %s OFFSET %s", (limit, skip))
        clientes = []
        for row in db_cursor.fetchall():
            cliente = Cliente(id=row[0], nombre_cliente=row[1], correo=row[2])
            clientes.append(cliente)
        return clientes

def get_all_items(skip: int = 0, limit: int = 10) -> List[Item]:
    with db_lock:
        db_cursor.execute("SELECT id, nombre, codigo FROM items LIMIT %s OFFSET %s", (limit, skip))
        items = []
        for row in db_cursor.fetchall():
            item = Item(id=row[0], nombre=row[1], codigo=row[2])
            items.append(item)
        return items

def create_initial_data():
    clientes = [
        Cliente(nombre_cliente="Carlos", correo="carlos@example.com"),
        Cliente(nombre_cliente="Ana", correo="ana@example.com"),
        Cliente(nombre_cliente="Juan", correo="juan@example.com"),
        Cliente(nombre_cliente="Maria", correo="maria@example.com"),
        Cliente(nombre_cliente="Luis", correo="luis@example.com"),
    ]
    
    items = [
        Item(nombre="Laptop", codigo="LT1001"),
        Item(nombre="Mouse", codigo="MS2002"),
        Item(nombre="Teclado", codigo="TK3003"),
        Item(nombre="Monitor", codigo="MN4004"),
        Item(nombre="Impresora", codigo="IP5005"),
        Item(nombre="Teléfono", codigo="TP6006"),
        Item(nombre="Tableta", codigo="TB7007"),
        Item(nombre="Cámara", codigo="CM8008"),
        Item(nombre="Altavoz", codigo="AL9009"),
        Item(nombre="Micrófono", codigo="MC1010"),
    ]

    for cliente in clientes:
        insert_cliente(cliente)
        
    for item in items:
        insert_item(item)

def close_connection():
    db_connection.close()

