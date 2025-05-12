import pytest
import sqlite3

def test_foreign_key_constraint(db_connection):
    cursor = db_connection.cursor()
    
    # Criando tabelas
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, item TEXT, FOREIGN KEY (user_id) REFERENCES users(id))")
    db_connection.commit()
    
    # Tentando inserir pedido sem usuário
    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute("INSERT INTO orders (user_id, item) VALUES (99, 'Celular')")
        db_connection.commit()
    
    cursor.close()