import pytest
import sqlite3

def test_index_performance(db_connection):
    cursor = db_connection.cursor()
    
    # Criando tabela e índice
    cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE INDEX idx_name ON test(name)")
    db_connection.commit()
    
    # Inserindo dados
    for i in range(1, 1001):
        cursor.execute("INSERT INTO test (name) VALUES (?)", (f"User_{i}",))
    db_connection.commit()
    
    # Verificando uso do índice
    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM test WHERE name = 'User_500'")
    result = cursor.fetchall()
    
    cursor.close()
    
    assert "USING INDEX" in str(result), "A busca deveria utilizar o índice."