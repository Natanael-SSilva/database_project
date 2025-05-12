import pytest
import sqlite3

def test_view(db_connection, setup_database):
    cursor = db_connection.cursor()
    
    # Inserindo dados
    cursor.execute("INSERT INTO users (name) VALUES ('Charlie')")
    cursor.execute("INSERT INTO orders (user_id, item) VALUES (1, 'Smartphone')")
    db_connection.commit()
    
    # Consultando view
    cursor.execute("SELECT * FROM user_orders")
    result = cursor.fetchone()
    
    cursor.close()
    
    assert result is not None, "A view deveria conter pelo menos um registro."
    assert result[0] == "Charlie", "O nome do usuário deveria ser 'Charlie'."
    assert result[1] == "Smartphone", "O item deveria ser 'Smartphone'."