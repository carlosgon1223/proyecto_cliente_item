# tests/test_database.py

from database import insert_cliente, insert_item, get_all_clientes, get_all_items,Cliente

def test_insert_cliente():
    # Prueba la inserción de un cliente en la base de datos
    # y verifica que se haya insertado correctamente.
    # Agrega más aserciones según sea necesario.
    cliente = Cliente(nombre_cliente="Ejemplo", correo="ejemplo@example.com")
    insert_cliente(cliente)
    clientes = get_all_clientes()
    assert len(clientes) > 0

# Agrega más pruebas unitarias según sea necesario.
