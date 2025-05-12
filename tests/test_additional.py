import pytest
import sqlite3

def test_insert_user(db_connection, setup_database):
    """Testa a inserção de um usuário."""
    cursor = db_connection.cursor()
    
    cursor.execute("INSERT INTO users (name) VALUES ('Dave')")
    db_connection.commit()
    
    cursor.execute("SELECT name FROM users WHERE name = 'Dave'")
    result = cursor.fetchone()
    
    cursor.close()
    
    assert result is not None, "O usuário inserido deveria existir."
    assert result[0] == "Dave", "O nome do usuário deveria ser 'Dave'."

def test_delete_user(db_connection, setup_database):
    """Testa a deleção de um usuário."""
    cursor = db_connection.cursor()
    
    cursor.execute("INSERT INTO users (name) VALUES ('Eve')")
    db_connection.commit()
    
    cursor.execute("DELETE FROM users WHERE name = 'Eve'")
    db_connection.commit()
    
    cursor.execute("SELECT name FROM users WHERE name = 'Eve'")
    result = cursor.fetchone()
    
    cursor.close()
    
    assert result is None, "O usuário deveria ter sido deletado."

def test_join_query(db_connection, setup_database):
    """Testa uma consulta com JOIN."""
    cursor = db_connection.cursor()
    
    cursor.execute("INSERT INTO users (name) VALUES ('Frank')")
    cursor.execute("INSERT INTO orders (user_id, item) VALUES (1, 'Laptop')")
    db_connection.commit()
    
    cursor.execute("SELECT users.name, orders.item FROM users JOIN orders ON users.id = orders.user_id")
    result = cursor.fetchone()
    
    cursor.close()
    
    assert result is not None, "A consulta JOIN deveria retornar um registro."
    assert result[0] == "Frank", "O nome do usuário deveria ser 'Frank'."
    assert result[1] == "Laptop", "O item deveria ser 'Laptop'."

def test_transaction(db_connection, setup_database):
    """Testa uma transação com rollback."""
    cursor = db_connection.cursor()
    
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("INSERT INTO users (name) VALUES ('Grace')")
    
    cursor.execute("ROLLBACK")
    
    cursor.execute("SELECT name FROM users WHERE name = 'Grace'")
    result = cursor.fetchone()
    
    cursor.close()
    
    assert result is None, "A transação deveria ter sido revertida."

def test_concurrency_simulation(db_connection, setup_database):
    """Simula concorrência com múltiplas inserções."""
    cursor1 = db_connection.cursor()
    cursor2 = db_connection.cursor()
    
    cursor1.execute("INSERT INTO users (name) VALUES ('Hank')")
    cursor2.execute("INSERT INTO users (name) VALUES ('Ivy')")
    db_connection.commit()
    
    cursor1.execute("SELECT COUNT(*) FROM users")
    count = cursor1.fetchone()[0]
    
    cursor1.close()
    cursor2.close()
    
    assert count == 2, "Ambas as inserções deveriam ter sido realizadas."