import pytest
import sqlite3

def test_trigger(db_connection, setup_database):
    cursor = db_connection.cursor()
    
    # Inserindo usuário e pedido
    cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
    cursor.execute("INSERT INTO orders (user_id, item) VALUES (1, 'Teclado')")
    db_connection.commit()
    
    # Verificando log
    cursor.execute("SELECT COUNT(*) FROM logs")
    count = cursor.fetchone()[0]
    
    cursor.close()
    
    assert count == 1, "O trigger deveria ter inserido um log automaticamente."