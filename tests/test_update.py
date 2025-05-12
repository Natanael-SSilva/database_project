import pytest
import sqlite3

def test_update_user(db_connection, setup_database):
    cursor = db_connection.cursor()
    
    # Inserindo usuário
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    db_connection.commit()
    
    # Atualizando nome
    cursor.execute("UPDATE users SET name = 'Alicia' WHERE name = 'Alice'")
    db_connection.commit()
    
    # Verificando atualização
    cursor.execute("SELECT name FROM users WHERE name = 'Alicia'")
    result = cursor.fetchone()
    
    cursor.close()
    
    assert result is not None, "O nome atualizado deveria existir no banco."
    assert result[0] == "Alicia", "O nome do usuário deveria ser 'Alicia'."